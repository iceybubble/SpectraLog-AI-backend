$uri = "http://localhost:9200/spectralog-windows/_doc"

$events = @(
    @{
        category = "authentication"
        action   = "login_success"
        outcome  = "success"
        severity = 1
        message  = "User successfully logged in"
        level    = "info"
    },
    @{
        category = "authentication"
        action   = "login_failed"
        outcome  = "failure"
        severity = 4
        message  = "Invalid password attempt"
        level    = "warning"
    },
    @{
        category = "malware"
        action   = "malware_detected"
        outcome  = "failure"
        severity = 8
        message  = "Suspicious executable detected"
        level    = "critical"
    },
    @{
        category = "privilege"
        action   = "admin_access"
        outcome  = "success"
        severity = 6
        message  = "Admin privileges granted"
        level    = "high"
    }
)

$event = Get-Random $events

$log = @{
    "@timestamp"        = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ss.fffZ")
    "event.category"    = $event.category
    "event.action"      = $event.action
    "event.outcome"     = $event.outcome
    "event.severity"    = $event.severity
    "host.name"         = $env:COMPUTERNAME
    "user.name"         = $env:USERNAME
    "source.ip"         = "192.168.1.$(Get-Random -Minimum 2 -Maximum 254)"
    "log.level"         = $event.level
    "message"           = $event.message
}

Invoke-RestMethod -Method Post -Uri $uri -ContentType "application/json" -Body ($log | ConvertTo-Json)
