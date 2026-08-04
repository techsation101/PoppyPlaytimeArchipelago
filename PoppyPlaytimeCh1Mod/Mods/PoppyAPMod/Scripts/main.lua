local UEHelpers = require("UEHelpers")

-------------------------------------------------------------------
-- 1. FILE LOGGING FUNCTION
-------------------------------------------------------------------
function LogEvent(eventName)
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
        print("[IPC Mod] Event Successfully Logged: " .. eventName)
    else
        print("[IPC Mod] ERROR: Failed to write to poppy_events.json")
    end
end

-------------------------------------------------------------------
-- 2. TAPE PICKUP HOOK
-- Runs whenever any VHS_TapeBP actor's interaction is triggered
-------------------------------------------------------------------
-- NotifyOnNewObject listens for when VHS_TapeBP objects are processed or interacted with
NotifyOnNewObject("/Game/Playtime/Blueprints/Items/Tape/VHS_TapeBP.VHS_TapeBP_C", function(tapeActor)
    print("[IPC Mod] Tape Actor Detected in World: " .. tapeActor:GetFullName())
end)

-- Hook the interaction or destruction of VHS_TapeBP_C
-- When picked up, the tape is destroyed/hidden by the game
RegisterHook("/Script/Engine.Actor:K2_DestroyActor", function(self)
    local actor = self:get()
    if actor and actor:IsValid() then
        local fullName = actor:GetFullName()
        
        -- Check if the destroyed actor is the VHS Tape
        if fullName:find("VHS_TapeBP") or fullName:find("VHS_Security") then
            print("[IPC Mod] VHS Tape Picked Up / Destroyed: " .. fullName)
            LogEvent("Pickup Green Tape First Room Ch 1")
        end
    end
end)

-------------------------------------------------------------------
-- 3. INBOUND COMMAND POLLING (0.5s Loop)
-------------------------------------------------------------------
function PollCommands()
    local file = io.open("poppy_commands.json", "r")
    if not file then return end

    local content = file:read("*a")
    file:close()

    if content:find('"processed"%s*:%s*false') then
        -- In UE4SS v3+, use GetPlayerController or FindFirstOf
        local pc = UEHelpers.GetPlayerController()
        if pc and pc:IsValid() then
            print("[IPC Mod] Processing external item commands...")
            -- Item granting logic goes here once event logging is verified
        end
    end
end

LoopAsync(500, PollCommands)

print("[IPC Mod] Tape tracking script initialized for VHS_TapeBP_C!")