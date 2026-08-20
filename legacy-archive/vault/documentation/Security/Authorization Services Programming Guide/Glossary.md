---
title: Authorization Services Programming Guide
apple_id: TP30000995
resource_type: Guide
platform: macOS
topic: Security
technology: Security
published: '2011-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/glossary/glossary.html
archived_at: '2026-07-18T02:06:40.708385Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Authorization Services Programming Guide](Introduction%20to%20Authorization%20Services%20Programming%20Guide.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __administrator__

  A user in the admin group. The user who installs OS X is automatically assigned to the admin group. An administrator has fewer privileges than root, but more privileges than a normal user. An administrator cannot create, delete, or move files in the system domain.

- __authentication__

  The act of verifying identity with something the user has, knows, or is. For example, a user knows information such as a name and password. The user may have something physical such as a smart card. The identity can be something the user is—a physical feature such as a fingerprint or retinal scan. Authentication may require two or more forms of identification.

- __authorization__

  The act of granting a right. For example, a user asks for the right to perform an operation. The Security Server grants authorization after the user fulfills the rules specified in the policy database—such as providing a credential or authenticating.

- __authorization option__

  A parameter or field that instructs the Security Server how to proceed with a request. Options include requesting preauthorization, requesting partial authorization, appending rights, and interacting with the user.

- __authorization reference__

  The Security Server uses the authorization reference to access an authorization session associated with a process.

- __Authorization Services__

  An API that facilitates fine-grain control of privileged operations, such as accessing restricted areas of the operating system and self-restricted parts of your Mac app. The Security Server uses policy-based decisions to authorize rights for users.

- __biometric identifier__

  A measurement of biological matter used for identification—for example, fingerprints, retinal scans, and face recognition.

- __credential__

  Proof of user authentication. used by the Security Server. When the Security Server authenticates a user, it creates a credential as part of the authorization session.

- __factored application__

  An application that uses a helper tool to perform specific tasks. Interprocess communication mechanisms are used to communicate between processes. In a factored application that uses Authorization Services, factor the code that performs privileged operations is factored into a separate helper tool.

- __helper tool__

  A tool that executes some of an application’s functions as a separate process. In the case of security, a helper tool performs privileged operations for the application. See also [setuid tool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqhawueq2jjfduksci).

- __key__

  The name of a rule. The Security Server uses a rule’s key to match a right with a rule.

- __permissions__

  In BSD, a set of attributes governing who can read, write, and execute resources in the file system. The output of the `ls -l` command represents permissions as a nine-position code segmented into three binary three-character subcodes; the first subcode gives the permissions for the owner of the file, the second for the group that the file belongs to, and the last for everyone else. For example, `-rwsr-xr--` means that the owner of the file has read, write, execute permissions (rwx); the group has read and execute permissions (r-x); all others have only read permissions. (The left-most position is reserved for a special character that says if this is a regular file (-), a directory (d), a symbolic link (l), or a special pseudo file device.) The execute bit has a different semantic for directories, meaning they are searchable.

- __policy-based system__

  A system that requires authorization to perform a privileged operations.

- __policy database__

  A database containing the set of rules the Security Server uses to determine authorization.

- __preauthorization__

  A form of authorization used before performing the actual authorization. Preauthorization is used to determine if a user has the possibility of authorizing later.

- __privileged operation__

  An operation that requires special rights or permissions. For example, all operations a user performs as root are privileged.

- __right__

  A named privilege. The Security Server authorizes rights for a user to perform a privileged operation.

- __rule__

  A set of attributes used to set security policies for applications and for the system. See also [policy database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqhawueq2jizbuer2b).

- __root__

  (1) The user with unlimited system privileges. Also called the superuser. (2) The top directory in a BSD-style directory hierarchy. Written as a slash (/), it is the first element in every absolute pathname.

- __Security Server__

  A Core Services application in OS X that deals with authorization and authentication through interaction with the policy database and Pluggable Authentication Modules (PAM).

- __self-restricted application__

  An application that restricts part of its features to specific users.

- __setuid bit__

  The fourth bit in a resource’s permissions code. When this bit is set to `s`, the system allows the process running it to masquerade as another user. For example, `-r-sr-xr-x 1 root wheel traceroute` allows the process running the `traceroute` utility to run as root.

- __setuid tool__

  A tool that has its setuid bit set.

- __system-restricted application__

  An application that has a portion of its features restricted to specific users because of the BSD permissions system.

[Previous](Document%20Revision%20History.md)

