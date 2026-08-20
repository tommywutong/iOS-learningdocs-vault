---
title: AirPlay Overview
apple_id: TP40011045
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AirPlayGuide/EncryptionandAuthentication/EncryptionandAuthentication.html
archived_at: '2026-07-15T05:21:01.358756Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AirPlay Overview](About%20AirPlay.md)


[Next](Document%20Revision%20History.md)[Previous](Enriching%20the%20AirPlay%20Experience%20in%20Your%20App.md)

# Encryption and Authentication

If you use HTTP Live Streaming, iOS provides built-in support for media encryption, and beginning in iOS 5.0, it also provides support for authentication. If you serve the encryption key from a protected domain, your app is responsible for handling the initial authentication handshake with your server.

Using HTTP Live Streaming, you can instruct the media segmenter software to encrypt your media. The segmenter generates encryption keys—and initialization vectors for those keys—at specified intervals.

The keys are used to encrypt all video for a given period. The client software retrieves the keys and uses them to decrypt the video. An initialization vector is required to use a key.

You tell the segmenter how often to change the key and how often to change the initialization vector for the current key. You also give the segmenter a base URL to use for the keys and the initialization vectors. The segmenter includes the URLs of the keys and initialization vectors in the playlist files it generates.

The keys are normally changed infrequently, and are served over HTTPS for security. The initialization vectors are normally changed frequently, but are served over HTTP for speedy delivery. The use of HTTP does not reduce security, because the initialization vectors are useless without the keys.

For more information, see _[HTTP Live Streaming Overview](../../Networking%20Internet/HTTP%20Live%20Streaming%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzs)_.

To protect your encryption keys, your server should require video clients to authenticate themselves. The method of authentication varies with the app. Using AirPlay with encrypted streaming content is supported only in iOS 5.0 and later.

For Web-based video playing in Safari (in iOS), you need to have the user authenticate manually before playing video encrypted with a key served from a secure domain. The authentication can be provided in JavaScript, but not without the risk of exposing the login information. Although manual authentication works well for pay-per-view or subscription video, it is normally undesirable for advertisement-supported video because it requires a login for viewing.

Bear in mind that if the video is playing over AirPlay, the viewer is watching on a television with no way to enter a password. In such cases, the viewer must authenticate on the device that is relaying the video via AirPlay, which might be in another room. This situation has other implications, including how long cookies or other authentication tokens should last before expiration. You should configure your server accordingly.

For video playing in an app, there are three recommended means of authenticating key delivery:

- __Serve keys from a protected HTTPS realm.__ Before playback begins, your app can use [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection) to authenticate itself, providing credentials that are kept hidden.
- __Use cookies over HTTPS.__ Your app can make a connection to an HTTPS server and authenticate the app in an app-defined way. Your server can then issue a cookie that applies to the key URLs. You should set the cookie to expire long after playback is complete. The server must then require the presence of a valid session cookie in future `GET` requests for the keys.

  For maximum reliability, if the expiration date is in the near future, the server should update the cookie’s expiration date in its response to future `GET` requests.
- __Specify the keys in the .m3u8 files using an app-defined URL scheme__. The app should register a custom [NSURLProtocol](https://developer.apple.com/documentation/foundation/nsurlprotocol) to handle requests for those URLs. The player then calls back into your app when it needs to load a key URL; your app can then obtain the key using a secure side channel and can provide it to the player.

For more information, see _[HTTP Live Streaming Overview](../../Networking%20Internet/HTTP%20Live%20Streaming%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzs)_.

[Next](Document%20Revision%20History.md)[Previous](Enriching%20the%20AirPlay%20Experience%20in%20Your%20App.md)

