---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/SyncingWidgets.html
archived_at: '2026-07-15T05:17:30.937445Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Using%20Widget%20Events.md)[Previous](Widget%20Backs%20and%20Preferences.md)

# Syncing Widgets

OS X v.10.5 includes Dashboard Sync, a mechanism for syncing a widget’s preferences between multiple Macs using .Mac. If a widget is installed on both Macs and the Macs are synced using Dashboard Sync in .Mac preferences, both Macs have a synchronized Dashboard.

In order for a widget to be synced between two Macs, you have to set up syncing using the same .Mac account in .Mac preferences on two or more Macs. Also, the same widget must be installed on all synced Macs.

Once these conditions are met, Dashboard Sync keeps widget preferences in sync between multiple Macs. This synchronization is automatic and doesn’t _require_ that you to do anything in your widget. Every time your widget retrieves a preference (as discussed in [Providing Preferences](Widget%20Backs%20and%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbtfvjvomq)), the most-recently synced version is provided to your widget.

Despite the fact that your widget’s preferences sync for free, you may want to do two things to adopt syncing into your widget:

- Provide a handler for a sync event, as discussed in [Handling a Sync Event](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donbyfvjvomq)
- Exclude certain preferences from syncing, as discussed in [Excluding Preferences from Syncing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donbyfvjvomy)

Your widget can be notified when Dashboard is synced using the `widget.onsync` handler. Listing 1 shows a handler for `widget.onsync` that reads a preference and updates a string on the widget interface with the preference’s value.

__Listing 1__  Providing an onsync handler

```
if (window.widget)
{
    widget.onsync = synced;
}

function synced()
{
    document.getElementById("aString").innerText = widget.preferenceForKey("aKey");
}
```

The handler that you provide for the `widget.onsync` event is called when a Dashboard sync is complete. This gives you the opportunity immediately after a sync to read your preferences and update values in your widget to any new values acquired in the sync.

Your widget may have values that you don’t want to include when Dashboard syncs preferences across Macs. To exclude a preference from syncing, use the `SyncExclusions` `Info.plist` key, as shown in Listing 2.

__Listing 2__  Excluding a preference using the SyncExclusions Info.plist key

```
<key>SyncExclusions</key>
        <array>
                <dict>
                        <key>key</key>
                        <string>aKey</string>
                        <key>global</key>
                        <true/>
                </dict>
        </array>
```

The `SyncExclusions` key takes an array of dictionaries as its value. Each dictionary consists of two keys: `key` and `global`. For each key that you want to exclude from syncing, repeat the dictionary containing `key` and `global` values.

The value for `key` is the name of a preference that you store, while the `global` key is a boolean value that specifies if the preference is a global or per-instance preference. Global preferences are not unique to one widget, while a per-instance preference is unique for each instance of your widget. A preference is a per-instance preference if the first portion of its key uses the `widget.identifier` property, yielding a key like `<widget.indentifier>-<key>`. If the per-instance preference is not formatted in this way, it can not be excluded.

To make per-instance preferences that use this format, include a function like the `makeKey` function in Listing 3.

__Listing 3__  A function for making unique per-instance preferences

```
function makeKey(key)
{
    return (widget.identifier + "-" + key);
}
```

Then, whenever you set or get a preference, use the `makeKey` function to make the preference per-instance, as demonstrated in Listing 4.

__Listing 4__  Using per-instance preferences

```
widget.setPreferenceForKey(aString, makeKey("aKey"));
...
var foo = widget.preferenceForKey(makeKey("aKey"));
```

[Next](Using%20Widget%20Events.md)[Previous](Widget%20Backs%20and%20Preferences.md)

