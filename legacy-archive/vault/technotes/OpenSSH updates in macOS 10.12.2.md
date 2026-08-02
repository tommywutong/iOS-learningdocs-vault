---
title: OpenSSH updates in macOS 10.12.2
apple_id: DTS40017589
resource_type: Technical Note
platform: macOS
topic: Cross Platform
technology: null
published: '2016-12-20'
source_url: https://developer.apple.com/library/archive/technotes/tn2449/_index.html
archived_at: '2026-07-26T19:54:15.208555Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2449

# OpenSSH updates in macOS 10.12.2

macOS 10.12.2 includes version 7.3p1 of OpenSSH. This technote documents some `ssh` behavior changes over previous macOS versions introduced in this update.

[Keychain changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjyhewugsbrfvfukwkdjbaustq)[Agent changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjyhewugsbrfvauorkokq)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjyhewugsbrfvjekrq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjyhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Keychain changes

Prior to macOS Sierra, `ssh` would present a dialog asking for your passphrase and would offer the option to store it into the keychain. This UI was deprecated some time ago and has been removed.

Instead, a new `UseKeychain` option was introduced in macOS Sierra allowing users to specify whether they would like for the passphrase to be stored in the keychain. This option was enabled by default on macOS Sierra, which caused all passphrases to be stored in the keychain.

This was not the intended default behavior, so this has been changed in macOS 10.12.2. To store passphrases in the keychain, set this option in your `ssh` configuration file:

```
 UseKeychain yes
```

This option can be set for all hosts, or for a subset of hosts as desired. For instance, you can configure a development machine as such:

```
 Host server.example.com
    IdentityFile ~/.ssh/id_rsa
    UseKeychain yes
```

This will only store the passphrase in the keychain for that specific key.

If you are sharing your `ssh` configuration with systems running older versions of OpenSSH that don't understand the `UseKeychain` option, you can specify the `IgnoreUnknown` option to keep your configuration compatible with both new and old versions, like this:

```
 IgnoreUnknown UseKeychain
    UseKeychain yes
```

[Back to Top](#)

## Agent changes

OpenSSH will no longer load keys into `ssh-agent` automatically. This aligns the macOS behavior with that of the upstream OpenSSH project.

It is possible for the user to re-enable loading keys into the agent by setting this option in the `ssh` configuration file:

```
 AddKeysToAgent yes
```

If you are seeing cases where you have disabled storing the passphrase in your keychain and `ssh` asks for your passphrase over and over, this is likely the reason.

[Back to Top](#)

## References

`ssh` [manual page](x-man-page://1/ssh)

`ssh_config` [manual page](x-man-page://5/ssh_config)

`ssh-agent` [manual page](x-man-page://1/ssh-agent)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-12-20 | New document that describes changes to OpenSSH in macOS 10.12.2. |

