local UEHelpers = require("UEHelpers")

-------------------------------------------------------------------
-- 1. FILE LOGGING FUNCTION
-------------------------------------------------------------------
local loggedEvents = {}

function LogEvent(eventName)
    if loggedEvents[eventName] then return end
    loggedEvents[eventName] = true

    local file = io.open("poppy_events.json", "w")
    if file then
        local jsonString = string.format([[
{
  "latest_event": "%s",
  "timestamp": "%s"
}
]], eventName, os.date("!%Y-%m-%dT%H:%M:%SZ"))

        file:write(jsonString)
        file:close()
        print("[AP Mod] SUCCESS: Event Logged -> " .. eventName)
    else
        print("[AP Mod] ERROR: Could not write to poppy_events.json")
    end
end

-------------------------------------------------------------------
-- 2. TAPE PICKUP HOOK
-------------------------------------------------------------------
RegisterHook("/Script/Engine.Actor:K2_DestroyActor", function(self)
    local actor = self:get()
    if actor and actor:IsValid() then
        local fullName = actor:GetFullName()
        if fullName:find("VHS_TapeBP") or fullName:find("VHS_Security") then
            print("[AP Mod] Tape Picked Up: " .. fullName)
            LogEvent("Pickup Green Tape First Room Ch 1")
        end
    end
end)

-------------------------------------------------------------------
-- 3. NATIVE ENGINE COMPONENT HOOKS (Zero Path Errors)
-------------------------------------------------------------------

-- Hook 1: Detect when any component on VHSPlayerBP7 changes visibility
RegisterHook("/Script/Engine.SceneComponent:SetVisibility", function(self, bNewVisibility)
    local comp = self:get()
    if not comp or not comp:IsValid() then return end

    pcall(function()
        local owner = comp:GetOwner()
        if owner and owner:IsValid() then
            local ownerName = owner:GetFullName()
            if ownerName:find("VHSPlayerBP7") or ownerName:find("entrance") then
                print("[AP Mod] SetVisibility triggered on Entrance VCR!")
                LogEvent("Listen to Green Tape First Room Ch 1")
            end
        end
    end)
end)

-- Hook 2: Detect when a component's hidden state is toggled
RegisterHook("/Script/Engine.SceneComponent:SetHiddenInGame", function(self, NewHidden)
    local comp = self:get()
    if not comp or not comp:IsValid() then return end

    pcall(function()
        local owner = comp:GetOwner()
        if owner and owner:IsValid() then
            local ownerName = owner:GetFullName()
            if ownerName:find("VHSPlayerBP7") or ownerName:find("entrance") then
                print("[AP Mod] SetHiddenInGame triggered on Entrance VCR!")
                LogEvent("Listen to Green Tape First Room Ch 1")
            end
        end
    end)
end)

-- Hook 3: Detect when playback/animation components activate
RegisterHook("/Script/Engine.ActorComponent:Activate", function(self, bReset)
    local comp = self:get()
    if not comp or not comp:IsValid() then return end

    pcall(function()
        local owner = comp:GetOwner()
        if owner and owner:IsValid() then
            local ownerName = owner:GetFullName()
            if ownerName:find("VHSPlayerBP7") or ownerName:find("entrance") then
                print("[AP Mod] Component Activated on Entrance VCR!")
                LogEvent("Listen to Green Tape First Room Ch 1")
            end
        end
    end)
end)

print("[AP Mod] Native Engine Component Hooks Loaded Successfully!")