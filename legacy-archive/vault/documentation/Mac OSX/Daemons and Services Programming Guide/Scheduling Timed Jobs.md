---
title: Daemons and Services Programming Guide
apple_id: 10000172i
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html
archived_at: '2026-07-15T08:16:29.703547Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Daemons and Services Programming Guide](About%20Daemons%20and%20Services.md)


[Next](Startup%20Items.md)[Previous](Creating%20Launch%20Daemons%20and%20Agents.md)

# Scheduling Timed Jobs

In OS X, you can run a background job on a timed schedule in two ways: `launchd` jobs and `cron` jobs. (Older approaches, such as `at` jobs and `periodic` jobs are deprecated and should not be used.) This section explains these methods briefly and provides links to manual pages that provide additional details.

The preferred way to add a timed job is to use `launchd`. Each `launchd` job is described by a separate file. This means that you can manage `launchd` timed jobs by simply adding or removing a file.

To create a `launchd` timed job, you should create a configuration property list file similar to those described in [Creating a launchd Property List File](Creating%20Launch%20Daemons%20and%20Agents.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytonrsfuytanbrgqza) except that you specify a `StartCalendarInterval` key containing a dictionary of time values.

For example, the following property list runs the program `happybirthday` at midnight every time July 11 falls on a Sunday.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.example.happybirthday</string>
    <key>ProgramArguments</key>
    <array>
        <string>happybirthday</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Day</key>
        <integer>11</integer>
        <key>Hour</key>
        <integer>0</integer>
        <key>Minute</key>
        <integer>0</integer>
        <key>Month</key>
        <integer>7</integer>
        <key>Weekday</key>
        <integer>0</integer>
    </dict>
</dict>
</plist>
```

For more information on these values, see the manual page for `launchd.plist`.

Systemwide `cron` jobs can be installed by modifying `/etc/crontab`. Per-user `cron` jobs can be installed using the `crontab` tool. The format of these `crontab` files is described in the man page for the `crontab` file format.

Because installing `cron` jobs requires modifying a shared resource (the `crontab` file), you should not programmatically add a `cron` job.

If the system is turned off or asleep, `cron` jobs do not execute; they will not run until the next designated time occurs.

If you schedule a `launchd` job by setting the `StartCalendarInterval` key and the computer is asleep when the job should have run, your job will run when the computer wakes up. However, if the machine is off when the job should have run, the job does not execute until the next designated time occurs.

All other `launchd` jobs are skipped when the computer is turned off or asleep; they will not run until the next designated time occurs.

Consequently, if the computer is always off at the job’s scheduled time, both `cron` jobs and `launchd` jobs never run. For example, if you always turn your computer off at night, a job scheduled to run at 1 A.M. will never be run.

[Next](Startup%20Items.md)[Previous](Creating%20Launch%20Daemons%20and%20Agents.md)

