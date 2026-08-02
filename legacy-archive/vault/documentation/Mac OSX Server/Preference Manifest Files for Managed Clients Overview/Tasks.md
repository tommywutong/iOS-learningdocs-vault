---
title: Preference Manifest Files for Managed Clients Overview
apple_id: TP40001805
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/MacOSXServer/Conceptual/Preference_Manifest_Files/Chapter_2/PM_Chapter2.html
archived_at: '2026-07-15T08:16:38.902367Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preference Manifest Files for Managed Clients Overview](About%20This%20Manual.md)


[Next](Document%20Revision%20History.md)[Previous](Concepts.md)

# Tasks

This chapter provides an example of a preference manifest file.

This example is a preference manifest file for the Dock keys that control hiding, position, tile size, andfolders added by the managed client software. The name of the file is `com.apple.dock.manifest`.

```xml
<?xml version=”1.0” encoding=”UTF-8”?>
<!DOCTYPE plist PUBLIC “-//Apple Computer//DTD PLIST 1.0//EN”
“http://www.apple.com/DTDs/PropertyList-1.0.dtd”>
<plist version=”1.0”>
<dict>
    <key>pfm_description</key>
    <string>Dock preferences. Preferences are divided between  simple “appears” keys  and the more complicated Application and Document tile dictionaries, </string>
    <key>pfm_domain</key>
    <string>com.apple.dock</string>
    <key>pfm_name</key>
    <string>Dock</string>
    <key>pfm_subkeys</key>
    <array>
        <dict>
            <key>pfm_default</key>
            <false/>
            <key>pfm_description</key>
            <string>True to turn hiding on.</string>
            <key>pfm_name</key>
            <string>autohide</string>
            <key>pfm_targets</key>
            <array>
                <string>user</string>
                <string>user-managed</string>
            </array>
            <key>pfm_title</key>
            <string>Hiding</string>
            <key>pfm_type</key>
            <string>boolean</string>
        </dict>
        <dict>
            <key>pfm_default</key>
            <string>bottom</string>
            <key>pfm_description</key>
            <string>Left, right, or bottom Dock position</string>
            <key>pfm_name</key>
            <string>orientation</string>
            <key>pfm_range_list</key>
            <array>
                <string>left</string>
                <string>bottom</string>
                <string>right</string>
            </array>
            <key>pfm_targets</key>
            <array>
                <string>user</string>
                <string>user-managed</string>
            </array>
            <key>pfm_title</key>
            <string>Position</string>
            <key>pfm_type</key>
            <string>string</string>
        </dict>
        <dict>
            <key>pfm_default</key>
            <real>64.0</real>
            <key>pfm_description</key>
            <string>Tile size.</string>
            <key>pfm_name</key>
            <string>tilesize</string>
            <key>pfm_range_max</key>
            <real>128.0</real>
            <key>pfm_range_min</key>
            <real>16.0</real>
            <key>pfm_targets</key>
            <array>
                <string>user</string>
                <string>user-managed</string>
            </array>
            <key>pfm_title</key>
            <string>Tile Size</string>
            <key>pfm_type</key>
            <string>real</string>
        </dict>
        <dict>
            <key>pfm_description</key>
            <string>Folders added by Managed Client.</string>
            <key>pfm_name</key>
            <string>MCXDockSpecialFolders-Raw</string>
            <key>pfm_repetition_max</key>
            <integer>0</integer>
            <key>pfm_subkeys</key>
            <array>
                <dict>
                    <key>pfm_description</key>
                    <string>Flag for one folder added by Managed  Client.</string>
                    <key>pfm_name</key>
                    <string>mcxfolderflag</string>
                    <key>pfm_range_list</key>
                    <array>
                        <string>AddDockMCXMyApplicationsFolder</string>
                        <string>AddDockMCXDocumentsFolder</string>
                        <string>AddDockMCXOriginalNetworkHomeFolder</string>
                    </array>
                    <key>pfm_repetition_max</key>
                    <integer>3</integer>
                    <key>pfm_repetition_min</key>
                    <integer>0</integer>
                    <key>pfm_title</key>
                    <string>Folder Flag</string>
                    <key>pfm_type</key>
                    <string>string</string>
                </dict>
            </array>
            <key>pfm_targets</key>
            <array>
                <string>user</string>
                <string>user-managed</string>
            </array>
            <key>pfm_title</key>
            <string>Managed Client Special Folders</string>
            <key>pfm_type</key>
            <string>array</string>
        </dict>
    </array>
    <key>pfm_title</key>
    <string>Dock</string>
    <key>pfm_version</key>
    <real>0.5</real>
</dict>
</plist>
```

[Next](Document%20Revision%20History.md)[Previous](Concepts.md)

