$uri = "http://localhost:9200/logs-events/_doc"

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

# Send 100 fake Windows logs
for ($i = 1; $i -le 100; $i++) {

    $nowUtc = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ss.fffZ")
    $event = Get-Random $events

    $log = @{
        # when the event occurred
        "@timestamp"   = $nowUtc
        "timestamp"        = $nowUtc

        # when SOC ingested it
        "ingested_at"      = $nowUtc

        "event" = @{
            "category" = $event.category
            "action"   = $event.action
            "outcome"  = $event.outcome
            "severity" = $event.severity
        }

        "host" = @{
            "name" = $env:COMPUTERNAME
        }

        "user" = @{
            "name" = $env:USERNAME
        }

        "source" = @{
            "ip" = "192.168.1.$(Get-Random -Minimum 2 -Maximum 254)"
        }

        "log" = @{
            "level" = $event.level
        }

        "message" = $event.message

        
        "data_origin" = "synthetic"
        "platform"    = "windows"
    }

    Invoke-RestMethod `
        -Method Post `
        -Uri $uri `
        -ContentType "application/json" `
        -Body ($log | ConvertTo-Json -Depth 5)

    Start-Sleep -Milliseconds 100
}

Write-Host " 100 fake Windows logs (with ingested_at) sent to logs-events"
