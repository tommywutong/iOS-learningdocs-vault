---
title: Security Credentials
apple_id: DTS10002309
resource_type: QA
platform: macOS
topic: Security
technology: Security
published: '2011-07-26'
source_url: https://developer.apple.com/library/archive/qa/qa1277/_index.html
archived_at: '2026-07-18T02:30:21.178167Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1277

# Security Credentials

## Q:  I'm writing a program that uses Authorization Services. When I call `AuthorizationCopyRights`, sometimes I get a password dialog and sometimes I don't. What's going on?.

A: This relates to a poorly understood aspect of Authorization Services and the Security Server. To understand what's going on, you need to understand how the Security Server implements authorization.

A credential is something that the Security Server knows about a particular user. The standard example of a credential is the knowledge that a particular user has entered a valid user name and password.

The Security Server maintains a global (per-login session) credentials cache, and a credentials cache per authorization instance [1]. When you request authorization for a particular right, the right specification (found in the authorization policy database in `/etc/authorization`) indicates the list of credentials that must be obtained to grant the right. It may also include a `shared` key, which determines whether the credentials are shared. For each credential in the right specification, the Security Server attempts to obtain the credential from a credentials cache. It first looks in the credentials cache associated with the authorization instance. If the credential isn't there and credentials are shared, it then looks in the global credentials cache. If the Security Server can't find the credential in a cache, it tries to acquire the credential. Typically this involves putting up an authentication dialog, where the user must enter a user name and password. However, on some configurations of Mac OS X, it may acquire the credential from other places (such as a smart card).

If the Security Server successfully obtains a credential, it remembers it in the credentials cache associated with the authorization instance and, if the right specifies that credentials are shared, in the global credentials cache.

If the right specification has a `timeout` key, its value indicates how long (in seconds) a cached credential is applicable for this right. A value of 0 means that the credential can only be used once (that is, it times out immediately). If the timeout key is missing, the credential can always be used to grant the right (unless the credential is destroyed, see below).

The above seems like security-geek trivia, until you understand some important consequences:

- When you log in, `loginwindow` acquires the right `system.login.console`. As a side effect, this acquires the credential indicating that you know your user name and password, and stores that credential in the global credentials cache.
- Most other right specifications (for example, `system.preferences`, which controls whether you can modify settings in System Preferences) require that you prove that you know the user name and password of an administrator. If you're in the `admin` group, the act of logging in acquires this credential and stores it in the global credentials cache. Thus, if you're in the `admin` group, you don't need to enter your password to make changes in System Preferences.
- If an applications requests a right and the right specification in the policy database indicates that any newly acquired credentials should be shared and you enter your user name and password, that credential goes into the global credentials cache. If another application (that is, another authorization instance) requests a right and the right specification dictates that your user name and password credential is required, Security Server will use the credential from the global credential cache. Thus, entering your user name and password in one application will allow other applications to use the credential.

The end result is that in many cases a call to `AuthorizationCopyRights` does not require you to enter a user name and password because the Security Server already has cached the required credentials.

The only way to guarantee that a credential acquired when you request a right is not shared with other authorization instances is to destroy that credential. You do this by calling `AuthorizationFree` and passing in the flag `kAuthorizationFlagDestroyRights`.

__Notes:__

1. An authorization instance is more-or-less equivalent to an `AuthorizationRef`, although you can have multiple processes sharing the same authorization instance if you externalize the `AuthorizationRef` and pass it between the processes.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-26 | Reformatted content and made minor editorial changes. |
| 2003-08-06 | New document that discusses AuthorizationCopyRights and the relationship between Authorization Services, authorization sessions, Security Server, credentials, and the credentials cache. |

