---
title: Sherlock Channels
apple_id: 10000121i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-04-09'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Sherlock/Tasks/InstallingAccessing.html
archived_at: '2026-07-15T05:18:58.141854Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sherlock Channels](Introduction%20to%20Sherlock%20Channels.md)


[Next](Printing%20Your%20Channel%E2%80%99s%20Content.md)[Previous](Creating%20a%20New%20Channel.md)

# Accessing Channels

Once you have created a channel, you need to test it and make it available for clients to use. The way you test and deploy a channel is over the web. By posting the files for your channel on a local web server, you can access them from the Sherlock application and verify that everything works. When you’re ready to deploy, you provide links to your channel using the `sherlock` web scheme.

If you are developing multiple related channels, you can group your channels together and distribute them as a subscription. Subscriptions simplify the process of loading multiple channels by making it possible to load all of the channels with one URL. The subscription itself simply contains a pointer to the individual channels you want to load.

Once your channel is deployed, you access it by entering the URL of your channel configuration file. In order to launch your channel in the Sherlock application, your URL must use the `sherlock` web scheme, that is, it must use the string `sherlock://` in place of the `http://` in the URL. Thus, the URL for accessing a test channel might look something like the following:

```
sherlock://localhost/~steve/MyChannel.xml
```

This URL tells the browser to let Sherlock handle the URL. Sherlock locates your channel configuration file and uses the information in that file to load your channel and display it in the Sherlock application window.

In addition to simply displaying your channel, you can add an `action` attribute to a sherlock URL to perform additional actions. Table 1 lists the actions you can perform on a channel. If you do not specify an action, Sherlock performs the `display` action by default.

__Table 1__  Supported actions for Sherlock URLs

| Action | Description |
| `add` | Adds the specified channel to the current user’s preferences. This action also adds the Sherlock toolbar and menu for the current user. This action also displays the channel in the current window, or in a new window if the `new_window` attribute is present. |
| `display` | Displays the specified channel in the frontmost window, or in a new window if the `new_window` attribute is present. |
| `subscribe` | Subscribes the user to the channels in the subscription file specified by the URL. |
| `toolbar` | Set the value of this attribute to `hidden` if you want to hide the Sherlock toolbar on the window. Set it to `shown` to display the toolbar. If you do not specify this attribute, Sherlock shows or hides the toolbar based on the last user modification. Thus, if the user last hid the toolbar on a window, Sherlock hides the toolbar on the window being loaded. |

When adding or displaying channels, you can append the `new_window` attribute to the URL to open the channel in a new Sherlock window. For example, if you want to add your test channel to the toolbar and display the channel in a new window, you would use a URL similar to the following:

```
sherlock://localhost/~steve/MyChannel.xml?action=add&new_window
```


Sherlock supports the ability to subscribe to a group of channels all at once. Subscriptions are convenient if you have several related channels that you want users to install. Rather than force the user to install each channel separately, you can give them the URL of a subscription file and let them install the entire group of channels.

Another advantage of subscriptions is that you can adjust the contents of the subscription file at any time to change the currently available channels. Because the subscription file is located on the network, any changes you make to the file are reflected the next time the user launches Sherlock.

Users can hide and show channels belonging to a subscription using the Sherlock application. The Channels view provides options for moving subscriptions to a folder or toolbar. You can also use this view to unsubscribe to channels altogether.

The following listing shows the format of a channel subscription file and is taken from the developer channels subscription provided by Apple. Each `<channel>` tag contains a URL to a channel configuration file. The `<localized-strings>` tag is used primarily for the localization of the channel name itself. The name you specify is displayed in the Sherlock application preferences window.

```
<channels name="Developer">
    <channel url="channels/xquery.xml"/>
    <channel url="channels/javascript.xml"/>
    <channel url="channels/htmlview.xml"/>
    <localized-strings>
        <localized-string language="en" key="Developer"
                string="Apple Developer Channels" />
    </localized-strings>
</channels >
```

For more information on the syntax for the `channels` and `channel` tags, see [Channels Tags Syntax](Sherlock%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dkljrgm3tcnbx).

[Next](Printing%20Your%20Channel%E2%80%99s%20Content.md)[Previous](Creating%20a%20New%20Channel.md)

