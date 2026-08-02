---
title: Kernel Authorization
apple_id: DTS10003591
resource_type: Technical Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2010-03-23'
source_url: https://developer.apple.com/library/archive/technotes/tn2127/_index.html
archived_at: '2026-07-26T19:53:51.271618Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2127

# Kernel Authorization

Mac OS X 10.4 Tiger introduced a new kernel subsystem, Kernel Authorization or Kauth for short, for managing authorization within the kernel. The Kauth subsystem exports a kernel programming interface (KPI) that allows third party kernel developers to authorize actions within the kernel, modify authorization decisions, and extend the kernel's authorization landscape. It can also be used as a notification mechanism.

If you write code that interacts with the BSD portions of the Mac OS X kernel, you should read this technote to gain a passing familiarity with Kauth. If you need to perform any of the tasks list above, you'll want to study this technote in depth. Finally, if you're developing an anti-virus product for Mac OS X, you will need the information contained in this technote to implement "on access" and "post modification" file scanning.

[Kauth Fundamentals](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjukq2ujfhu4mi)[Implementing a Listener](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjukq2ujfhu4mq)[Registering a Listener](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjukq2ujfhu4my)[Deregistering a Listener](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjukq2ujfhu4na)[Registering a New Scope](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjukq2ujfhu4ni)[Deregistering a Scope](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjukq2ujfhu4nq)[Authorizing an Action](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjukq2ujfhu4ny)[Built-In Scopes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjukq2ujfhu4oa)[Process Scope](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjvkqstivbviskpjy4a)[Generic Scope](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjvkqstivbviskpjy4q)[File Operation Scope](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjvkqstivbviskpjyyta)[Vnode Scope](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjvkqstivbviskpjyytc)[Listener Gotchas](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjukq2ujfhu4mju)[Context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjvkqstivbviskpjyyti)[Kauth Cookbook](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjukq2ujfhu4mjy)[Denying the Debugger](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjvkqstivbviskpjyytq)[Anti-Virus Scanner](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjvkqstivbviskpjyyts)[New Kernel Subsystem](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjvkqstivbviskpjyzda)[KauthORama Sample Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewugsbrfvjukq2ujfhu4mrs)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjzgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Kauth Fundamentals

The Kauth system was introduced in Mac OS X 10.4 Tiger. It was implemented primarily to simplify the implementation of access control lists (ACLs), a major new feature of the Tiger kernel. Because evaluating an ACL is a complex task, the code for doing this has been abstracted out of each file system plug-in and moved into the kernel proper. Kauth does this in a general and flexible way.

While Kauth was originally designed to support ACLs, it is a general kernel authorization mechanism and can be used for a variety of other tasks. One such use is as a simple notification mechanism for anti-virus developers (see Anti-Virus Scanner).

To understand Kauth, you'll need to understand a number of core concepts.

- __scopes__ — A scope is an area of interest for authorization within the kernel. For example, the scope `KAUTH_SCOPE_VNODE` is used for all authorization within the VFS layer. Scopes allow you to register interest in some subset of kernel authorization decisions, without being involved in all authorization decisions.

  Scopes are strings formatted using reverse DNS notation (for example, `KAUTH_SCOPE_VNODE` is `"com.apple.kauth.vnode"`), so you can define your own scope if you like.
- __actions__ — An action is an operation within a scope. For example, the VFS subsystem defines an action, `KAUTH_VNODE_READ_DATA`, which determines whether you're allowed to read data from a file system object. Actions are specified by integer constants (the actual type is `kauth_action_t`) and each scope has its own action namespace.

  The combination of a scope and an action defines an operation whose authorization can be checked.
- __actors__ — An actor is an entity that's performing an operation.
- __credentials__ — Credentials are the information that identifies an actor. Credentials are specified by an opaque type, `kauth_cred_t`. There are numerous accessor functions that let you operate on this type. For example, `kauth_cred_getuid` returns the effective user ID (EUID) from the credentials.
- __request__ — In the context of this document, an actor makes requests to perform an action within a particular scope.
- __listener__ — A listener is a callback that makes an authorization decision for a request. Fundamentally the listener authorizes the request based on the credentials of the actor. The listener is free to use whatever scope- and action-dependent information necessary to make that decision.

  There is a __default listener__ for every built-in scope. This listener implements the standard BSD authorization model for all actions within that scope. In addition, you can register your own listeners for a scope.

[Back to Top](#)

## Implementing a Listener

The prototype for a listener is shown in Listing 1.

__Listing 1__  Prototype for a listener

```c
static int MyListener(     kauth_cred_t   credential,     void *         idata,     kauth_action_t action,     uintptr_t      arg0,     uintptr_t      arg1,     uintptr_t      arg2,     uintptr_t      arg3 );
```

The meaning of the first three arguments is the same for all scopes.

- `credential` is a reference to the actor's credentials.

  __Important:__ When inspecting the credentials associated with a request, always use the accessor functions defined in <sys/kauth.h>. Be especially careful when testing for group membership. In Tiger a user can be in lots of groups (many more than the traditional limit of 16) and groups can be nested. If you want to test whether a user is a member of a group, use `kauth_cred_ismember_gid`.
- `idata` is the cookie (or refCon) data you supplied when you registered the listener (see Registering a Listener).
- `action` is the requested action (for example, `KAUTH_VNODE_READ_DATA`).

The meaning of the remaining parameters is scope dependent. I'll discuss these in detail in later sections. However, in most cases these parameters give you extra information that allow you to make an authorization decision. For example, for the VFS scope (`KAUTH_SCOPE_VNODE`), `arg1` is a reference to the vnode (of type `vnode_t`) that's being operated on.

A listener callback must return one of the following values.

- `KAUTH_RESULT_DEFER` — This value indicates that the listener defers the decision about this request to the other listeners (and ultimately to the default listener).
- `KAUTH_RESULT_ALLOW` — This value indicates that, as far as this listener is concerned, the request is allowed.
- `KAUTH_RESULT_DENY` — This value indicates that the request should be denied.

For a request to be allowed, at least one listener must return `KAUTH_RESULT_ALLOW` and no listeners can return `KAUTH_RESULT_DENY`. This has a number of consequences.

- All listeners are called for all requests (because the last listener just might return `KAUTH_RESULT_DENY`).
- Because a listener can't allow a request that's denied by any other listener, a non-default listener can only tighten security.

When writing a listener, there are a number of important points that you need to keep in mind. These are discussed in the detail in Listener Gotchas.

[Back to Top](#)

## Registering a Listener

You can register a listener for an existing scope using `kauth_listen_scope`.

__Listing 2__  kauth_listen_scope

```
extern kauth_listener_t kauth_listen_scope(     const char *           identifier,      kauth_scope_callback_t callback,      void *                 idata );
```

The parameters are as follows:

- `identifier` is the name of the scope. The routine does not make a copy of the string pointed to by this parameter. This is not a problem if you're passing a constant string; however, if you're calculating the string at runtime, you must make sure that the string persists until you dispose of the resulting `kauth_listener_t`.
- `callback` is the address of your listener callback function, with the prototype shown in Listing 1.
- `idata` is the cookie (or refCon) for your listener callback.

On error, the result is `NULL`. On success, the result is a reference to the listener; you can use this to deregister your listener.

It is not an error to register a listener before the corresponding scope is registered. The system will remember your listener and apply it once the scope appears.

[Back to Top](#)

## Deregistering a Listener

You can deregister a listener using `kauth_unlisten_scope`.

__Listing 3__  kauth_unlisten_scope

```
extern void	kauth_unlisten_scope(kauth_listener_t listener);
```

The parameters are as follows:

- `listener` is a reference to the listener you got from `kauth_listen_scope`.

__Important:__ The return of `kauth_unlisten_scope` does not guarantee that all threads executing your listener have returned from your listener. Once `kauth_unlisten_scope` returns, you must take steps to avoid destroying state that these threads rely on until they've completed executing your listener's code. See KauthORama Sample Code for an example of our recommended approach for this.

[Back to Top](#)

## Registering a New Scope

__Important:__ You should only do this if you want to create your own custom scope. In most cases third party developers should register a listener for an existing scope.

You can register a new scope using `kauth_register_scope`.

__Listing 4__  kauth_register_scope

```
extern kauth_scope_t kauth_register_scope(     const char *           identifier,      kauth_scope_callback_t callback,      void *                 idata );
```

The parameters are as follows:

- `identifier` is the name of the scope. It is an error to register a scope that already exists. The routine does not make a copy of the string pointed to by this parameter. This is not a problem if you're passing a constant string; however, if you're calculating the string at runtime, you must make sure that the string persists at least until you dispose of the resulting `kauth_scope_t`.
- `callback` is the address of the listener callback function for this scope; this becomes the scope's default listener. This parameter may be `NULL`, in which case a callback that always returns `KAUTH_RESULT_DEFER` is assumed.
- `idata` is the cookie (or refCon) for the listener callback.

On error, the result is `NULL`. On success, the result is a reference to the scope; you can use this to deregister your scope.

[Back to Top](#)

## Deregistering a Scope

You can deregister a scope using `kauth_deregister_scope`:

__Listing 5__  kauth_deregister_scope

```
extern void	kauth_deregister_scope(kauth_scope_t scope);
```

The parameters are as follows:

- `scope` is a reference to the scope you got from `kauth_register_scope`.

Any other (non-default) listeners registered on the scope will go dormant; they'll be reactivated if the scope is reregistered.

__Important:__ The return of `kauth_deregister_scope` does not guarantee that all threads executing your listener have returned from your listener. See the discussion associated with `kauth_unlisten_scope` (in Deregistering a Listener) for details.

[Back to Top](#)

## Authorizing an Action

You can make an authorization request using `kauth_authorize_action`.

__Listing 6__  kauth_authorize_action

```
extern int kauth_authorize_action(     kauth_scope_t  scope,      kauth_cred_t   credential,      kauth_action_t action,     uintptr_t      arg0,      uintptr_t      arg1,      uintptr_t      arg2,      uintptr_t      arg3 );
```

The parameters are as follows:

- `scope` is a reference to the scope in which the action is defined. You get this value from the result of `kauth_register_scope`.
- `credential` is a reference to the actor's credentials. Normally you would either already have this information, or you'd call `kauth_cred_get` to get the credentials for the current thread.
- `action` is the requested action.
- `arg0` through `arg3` are passed unmodified to the listener callbacks.

If your kernel extension supports plug-ins and those plug-ins call `kauth_authorize_action`, you must have a way for your plug-ins to discover the scope reference (`kauth_scope_t`). The easiest way to do this is to export a wrapper function that's tailored to your specific requirements.

__Important:__ The kernel already provides `kauth_authorize_action` wrappers for all of the scopes that it defines. If you're authorizing within a kernel-defined scope you should call these wrappers rather than calling `kauth_authorize_action` directly. These wrappers are described below, along with corresponding scopes.

[Back to Top](#)

## Built-In Scopes

This section lists all of the scopes built in to the Mac OS X kernel.

### Process Scope

The process scope (`KAUTH_SCOPE_PROCESS`, which is `"com.apple.kauth.process"`) is the easiest to understand. It defines just two actions.

- `KAUTH_PROCESS_CANTRACE` — Authorizes whether the current process can trace the target process. `arg0` (of type `proc_t`) is the process being traced. `arg1` (of type `(int *)`) is a pointer to an an errno-style error code; if the listener denies the request, it must set this value to a non-zero value.
- `KAUTH_PROCESS_CANSIGNAL` — Authorizes whether the current process can signal the target process. `arg0` (of type `proc_t`) is the process to be signalled. `arg1` (of type `int`) is the signal that's being sent.

  __Important:__ `KAUTH_PROCESS_CANSIGNAL` is currently not implemented by any version of Mac OS X (r. [3931697](rdar://problem/3931697)).

The kernel also exports a `kauth_authorize_action` wrapper for this scope, namely `kauth_authorize_process`.

__Listing 7__  kauth_authorize_process

```
extern int kauth_authorize_process(     kauth_cred_t   credential,      kauth_action_t action,     proc_t         process,      uintptr_t      arg1,      uintptr_t      arg2,      uintptr_t      arg3 );
```

This wrapper around `kauth_authorize_action` does two useful things:

1. It supplies the appropriate scope parameter.
2. It eliminates the need to cast `process` (of type `proc_t`) to `arg0` (of type `uintptr_t`).

Typically this is not useful for third party developers.

### Generic Scope

The generic scope (`KAUTH_SCOPE_GENERIC`, which is `"com.apple.kauth.generic"`) has a single action, `KAUTH_GENERIC_ISSUSER`, which the kernel requests to test whether an actor has superuser privileges. None of the generic arguments (`arg0` through `arg3`) are significant.

__Important:__ The kernel does not currently use this request for all superuser tests; in many cases the kernel continues to directly compare the credential's effective user ID to 0.

The kernel also exports a `kauth_authorize_action` wrapper for this scope, namely `kauth_authorize_generic`.

__Listing 8__  kauth_authorize_generic

```
extern int kauth_authorize_generic(     kauth_cred_t   credential,      kauth_action_t action );
```

Typically this is not useful for third party developers.

### File Operation Scope

The file operation scope (`KAUTH_SCOPE_FILEOP`, which is `"com.apple.kauth.fileop"`) is different from other scopes in that it's not used to actually authorize an operation; rather, the system uses this scope to notify listeners of significant file system operations. This can be used to implement an anti-virus scanning program, as described in Anti-Virus Scanner.

`KAUTH_SCOPE_FILEOP` defines the following actions.

- `KAUTH_FILEOP_OPEN` — Notifies that a file system object (a file or directory) has been opened. `arg0` (of type `vnode_t`) is a vnode reference. `arg1` (of type `(const char *)`) is a pointer to the object's full path.
- `KAUTH_FILEOP_CLOSE` — Notifies that a file system object is about to be closed. `arg0` (of type `vnode_t`) is a vnode reference. `arg1` (of type `(const char *)`) is a pointer to the object's full path. `arg2` (of type `int`) is a set of bit flags; the only flag currently defined is `KAUTH_FILEOP_CLOSE_MODIFIED`, which is set if a modified file is being closed.
- `KAUTH_FILEOP_RENAME` — Notifies that a file system object has been renamed. `arg0` (of type `(const char *)`) is a pointer to the object's previous full path. `arg1` (of type `(const char *)`) is a pointer to the object's new full path.
- `KAUTH_FILEOP_EXCHANGE` — Notifies that two files have been exchanged (via [exchangedata](x-man-page://2/exchangedata)). `arg0` (of type `(const char *)`) is a pointer to the first file's full path. `arg1` (of type `(const char *)`) is a pointer to the second file's full path.
- `KAUTH_FILEOP_LINK` — Notifies that a new hard link has been added to a file (via the [link](x-man-page://2/link) system call). `arg0` (of type `(const char *)`) is a pointer to the full path of the original file. `arg1` (of type `(const char *)`) is a pointer to the full path of the newly created link.
- `KAUTH_FILEOP_EXEC` — Notifies that a program has been executed (via the [execve](x-man-page://2/execve) system call). `arg0` (of type `vnode_t`) is a vnode reference of the program being executed (for Mach-O executables, this is the actual executable; for CFM applications, this will always reference `LaunchCFMApp`; for interpreted scripts, such as shell or perl scripts, this is the script, not the interpreter). `arg1` (of type `(const char *)`) is a pointer to the program file's full path.

If you install a listener in this scope, it will be called to notify you of these events. The kernel ignores the return value of your listener, although we recommend that you always return `KAUTH_RESULT_DEFER`.

__Warning:__ Prior to Mac OS X 10.5 the file operation scope had a nasty gotcha
(r. [4605516](rdar://problem/4605516))
. If you install a listener in the this scope and handle the `KAUTH_FILEOP_RENAME`, `KAUTH_FILEOP_LINK`, or `KAUTH_FILEOP_EXEC` actions, you must test whether `arg0` and `arg1` are `NULL` before accessing them as strings. Under certain circumstances (most notably, very early in the boot sequence and very late in the shutdown sequence), the kernel might pass you `NULL` for these arguments. If you access such a pointer as a string, you will kernel panic.

This problem was fixed in Mac OS X 10.5.

The kernel also exports a `kauth_authorize_action` wrapper for this scope, namely `kauth_authorize_fileop`.

__Listing 9__  kauth_authorize_fileop

```
extern int kauth_authorize_fileop(     kauth_cred_t   credential,      kauth_action_t action,     uintptr_t      arg0,      uintptr_t      arg1 );
```

Typically `kauth_authorize_fileop` is not useful for third party developers. However, if you do call it, take note of the following non-obvious behaviour. The `arg0` parameter of `kauth_authorize_fileop` is a `vnode_t`. `kauth_authorize_fileop` passes that `vnode_t` to the `arg0` parameter of the listener. It also gets the path to that vnode and passes that to the `arg1` parameter of the listener. Finally, for the `KAUTH_FILEOP_CLOSE` action, `kauth_authorize_fileop` passes its `arg1` parameter to the `arg2` parameter of the listener.

### Vnode Scope

The vnode scope (`KAUTH_SCOPE_VNODE`, which is `"com.apple.kauth.vnode"`) is the most complex scope currently defined. The first thing to note is that, within the vnode scope, actions are not enumerations but rather bitfields. Thus, it's perfectly reasonable to combine actions by ORing them together. For example, an action of `KAUTH_VNODE_READ_DATA` | `KAUTH_VNODE_EXECUTE` indicates that actor wishes to both read and execute the file.

To authorize an action within the vnode scope, you would call `vnode_authorize`.

__Listing 10__  vnode_authorize

```
extern int vnode_authorize(     vnode_t        vp,      vnode_t        dvp,      kauth_action_t action,      vfs_context_t  context );
```

The parameters are as follows:

- `vp` is the vnode on which the action is being performed.
- `dvp` is the parent directory's vnode. In many cases this is `NULL`, indicating that the parent is unknown or irrelevant.
- `action` is the operation being performed; this is discussed in detail below.
- `context` is the VFS context associated with the actor. This is an opaque data structure that's intimately tied to the VFS implementation. Most VFS entry points are passed this context. In addition, there are numerous VFS context routines defined in <sys/vnode.h>.

`vnode_authorize` is a fairly simple wrapper around `kauth_authorize_action`. It performs two useful functions:

1. It assembles the correct scope listener arguments (`arg0` through `arg3`). These are discussed below.
2. It ensures that the error code is correct. Specifically, it translates the `EPERM` error returned by `kauth_authorize_action` into `EACCES` (which is the appropriate error for file system functions). Also, if the listener denies a request and provides a specific error code (via `arg3`, see below), it returns that error.

__Important:__ It is relatively unusual for a VFS plug-in to call `vnode_authorize`. In most cases the VFS layer has authorized all actions before calling your plug-in. However, there are some circumstances where a VFS plug-in should call `vnode_authorize`. For example, HFS [Plus]'s implementation of [searchfs](x-man-page://2/searchfs) uses `vnode_authorize` to ensure that the caller has access to the file system objects that it's returning.

The scope listener arguments for the vnode scope are as follows:

- `arg0`, of type `vfs_context_t`, is `context` — The VFS context, described above.
- `arg1`, of type `vnode_t`, is `vp` — The vnode itself.
- `arg2`, of type `vnode_t`, is `dvp` — The parent vnode, if available. This may be `NULL`.
- `arg3`, of type `(int *)`, is `errPtr` — A pointer to an errno-style error. If your callback denies the request, it can set this value to indicate the error to return to the client. If you don't set this, the client gets `EACCES`.

Within the vnode scope, the following standard actions are defined.

- `KAUTH_VNODE_READ_DATA` (also `KAUTH_VNODE_LIST_DIRECTORY`) — If the vnode is a directory, authorizes the actor to enumerate the contents of that directory. Otherwise, authorizes the actor to read the contents of a file.
- `KAUTH_VNODE_WRITE_DATA` (also `KAUTH_VNODE_ADD_FILE`) — If the vnode is a directory, authorizes the actor to add a file to that directory. `vp` is the directory to which the file is being added; `dvp` is `NULL`. Otherwise, authorizes the actor to write the contents of a file.
- `KAUTH_VNODE_EXECUTE` (also `KAUTH_VNODE_SEARCH`) — If the vnode is a directory, authorizes the actor to probe for the existence of an item within the directory as part of a path lookup. Otherwise, authorizes the actor to execute the contents of a file.
- `KAUTH_VNODE_DELETE` — Authorizes the actor to delete an item from a directory. `vp` is the item to be deleted and `dvp` is the directory it's being deleted from.
- `KAUTH_VNODE_APPEND_DATA` (also `KAUTH_VNODE_ADD_SUBDIRECTORY`) — If the vnode is a directory, authorizes the actor to add a directory to it. Otherwise, this action is intended to authorize the actor to append data to the contents of a file; however, this aspect is not currently implemented.
- `KAUTH_VNODE_DELETE_CHILD` — When used in a directory's ACL, this permission controls whether the actor can delete an item from the directory. That is, for the actor to be able to delete the item, they must have `KAUTH_VNODE_DELETE` permission on the item and `KAUTH_VNODE_DELETE_CHILD` permission on the item's parent directory.

  A Kauth listener, however, rarely sees this action. When an actor deletes an item, the kernel just authorizes the `KAUTH_VNODE_DELETE` action on the item itself; it does not authorize a separate `KAUTH_VNODE_DELETE_CHILD` action on the parent directory. Rather, the default listener for the vnode scope will check the `KAUTH_VNODE_DELETE_CHILD` permission on the parent directory directly, without another pass through Kauth. This improves performance and avoids a potential race condition.

  On the other hand, a `KAUTH_VNODE_DELETE_CHILD` action is generated in response to an [access](x-man-page://2/access) system call with the `_RMFILE_OK` flag.
- `KAUTH_VNODE_READ_ATTRIBUTES` — Authorizes the actor to read standard attributes of the vnode (such as the time stamps).
- `KAUTH_VNODE_WRITE_ATTRIBUTES` — Authorizes the actor to change standard attributes of the vnode (such as the time stamps).
- `KAUTH_VNODE_READ_EXTATTRIBUTES` — Authorizes the actor to read extended attributes of the vnode (those accessed via `getxattr`, including the resource fork).
- `KAUTH_VNODE_WRITE_EXTATTRIBUTES` — Authorizes the actor to change (or add) extended attributes of the vnode (those accessed via `getxattr`, including the resource fork).
- `KAUTH_VNODE_READ_SECURITY` — Authorizes the actor to read the vnode's ACL.
- `KAUTH_VNODE_WRITE_SECURITY` — Authorizes the actor to change the vnode's ACL.
- `KAUTH_VNODE_TAKE_OWNERSHIP` — Authorizes the actor to change ownership of the vnode.
- `KAUTH_VNODE_SYNCHRONIZE` — This represents an ACL permission that is defined for compatibility with other platforms. It is preserved but not tested by Mac OS X. Hence, it is never used as a Kauth action.
- `KAUTH_VNODE_LINKTARGET` — Authorizes the actor to make a new hard link to the vnode.
- `KAUTH_VNODE_CHECKIMMUTABLE` — Authorizes the actor to modify the file (in the `SF_IMMUTABLE` sense; see [chflags](x-man-page://2/chflags)). This flag is set if other checks have already been made to check that the file can by modified, but the modification should still fail for immutable files.
- `KAUTH_VNODE_ACCESS` — This is a special flag. If this flag is set the authorization request is advisory (for example, to satisfy an [access](x-man-page://2/access) system call) rather than authoritative. A listener can use this to avoid doing extra work in the advisory case.
- `KAUTH_VNODE_NOIMMUTABLE` — This is a special flag. It is passed to the listener along with the `KAUTH_VNODE_WRITE_SECURITY` bit (and no others) to indicate that the actor wishes to change one or more of the immutable flags, and that the state of these flags should not be considered when authorizing the request.

#### Vnode Scope Gotchas

Remember that actions within the vnode scope are a bitfield. Thus a vnode scope listener can be called to authorize multiple actions simultaneously.

The vnode scope is __extremely hot__. If your vnode scope listener is slow, it will significantly slow down all file system operations. If you install a vnode scope listener, you should work to make it as efficient as possible.

When writing a vnode scope listener, be aware that not every file system operation will trigger an authorization request. For example, if an actor successfully requests `KAUTH_VNODE_SEARCH` on a directory, the system may cache that result and grant future requests without invoking your listener for each one.

For more information about the pitfalls of writing a listener, see Listener Gotchas.

[Back to Top](#)

## Listener Gotchas

When writing a listener, there are a number of important points that you need to keep in mind. These are discussed in the following sections.

### Context

In most cases your listener will be called by the user's thread. That is, a user thread has made a system call, which caused it to enter the kernel to do the work, which has triggered a Kauth request. So, it's possible to get information about the actor based on the current thread or process. For example, you can call `proc_self` to get a reference to the current process and then extract useful information from that.

However, you should try to avoid doing this. Rather, your listener should make its decision based on the actor's credentials (as passed to it in the `credentials` parameter) and, if you're listening in the vnode scope, the VFS context.

There are two reasons for this recommendation.

- As far as the overall kernel design is concerned, it is cleaner for your listener to make decisions based on its input parameters, rather than on implicit parameters like the current thread.
- In some cases, it's possible for a kernel operation to be executed by another thread on behalf of the user. This sort of thing already happens for asynchronous I/O, where the kernel maintains a pool of async I/O threads that perform asynchronous file system requests. Currently these threads don't actually make authorization requests, but the long-term direction is clear.

#### Deadlock Avoidance

Your listener is called by the thread that's performing the operation, so it's possible to block the thread while you process the request. However, this is a two-edged sword. It allows your listener to pass the request to an external agent (a user space daemon, for example) and block waiting for the results. However, doing so entails significant risk of deadlocking the system.

This problem most commonly crops up when writing a listener for the vnode or file operation scopes. A typical example is:

1. You install a listener for the file operation scope.
2. A normal process opens a file.
3. Your listener is called with `KAUTH_FILEOP_OPEN`. It passes the request to a user space daemon and waits for the result.
4. The user space daemon calls some system routine that RPCs to a system daemon. For example, it might call [getpwuid](x-man-page://3/getpwuid), which is actually implemented inside [lookupd](x-man-page://8/lookupd).
5. The system daemon opens a file.
6. This causes the kernel to call your listener, and the cycle starts over again.

This problem is much worse than it seems. Specifically:

- System daemons call other system daemons. For example, `lookupd` is dependent on [DirectoryService](x-man-page://8/DirectoryService), which may in turn be dependent on other daemons.
- You can't just hard-code a list of possible system daemons because the dependency tree varies of from release-to-release; Apple can add new dependencies at any time.
- It's impossible for your daemon to not depend on any system daemons. Every time you touch pageable memory, you might trigger the allocation of a paging file, which depends on the [dynamic_pager](x-man-page://8/dynamic_pager).

There are a variety of ways to avoid this deadlock. The best is for your listener to avoid do any processing if the request comes from a thread running as root (that is, where `kauth_cred_getuid` for the actor's credentials returns 0). As all critical system daemons will necessarily run as root, you break the deadlock at step 6 above.

__Note:__ The group resolution membership daemon, [memberd](x-man-page://8/memberd), faces a similar problem, and it avoids this problem in exactly this fashion; the system never invokes `memberd` if the thread is running as root.

However, this technique may not be appropriate in all cases. For example, an anti-virus scanner would particularly want to scan files being opened by a thread running with elevated privileges. In this case the only correct solution is for the scanner to operate entirely within the kernel.

#### Performance

Some Kauth scopes are very hot. That is, a typical system will make authorization requests in that scope frequently. For example, a system copying files might make thousands of vnode scope authorization requests per second. If you register a listener for a scope, it can be called for every request. If your listener is slow, it will significantly degrade system performance.

The two hot scopes on Mac OS X are the vnode scope and the file operation scope. If you install a listener for either of these scopes, be sure to measure the effect your listener has on overall system performance, and optimize your listener accordingly.

[Back to Top](#)

## Kauth Cookbook

This section describes how to use Kauth to implement some commonly requested features.

### Denying the Debugger

You can use Kauth to implement a kernel extension that prevents users attaching to processes with the debugger. All you need to do is register a listener for the `KAUTH_SCOPE_PROCESS` scope and look for the `KAUTH_PROCESS_CANTRACE` action. Listing 11 shows an example listener that denies debugging for everyone except root. You can use a similar technique to prevent the debugger attaching to specific processes.

__Listing 11__  Denying the debugger

```c
static int KauthDenyDebugListener(     kauth_cred_t    credential,     void *          idata,     kauth_action_t  action,     uintptr_t       arg0,     uintptr_t       arg1,     uintptr_t       arg2,     uintptr_t       arg3 )     // We register this listener for the KAUTH_SCOPE_PROCESS scope.      // The system calls this listener whenever it needs to authorize      // an action within that scope. We look for      // KAUTH_PROCESS_CANTRACE action and deny it if the requesting      // user is not root. {     int     result;      result = KAUTH_RESULT_DEFER;      switch (action) {         case KAUTH_PROCESS_CANTRACE:             {                 proc_t  targetProc;                 int *   errPtr;                  targetProc = (proc_t) arg0;                 errPtr     = (int *) arg1;                  if (kauth_cred_getuid(credential) != 0) {                     printf(                         "Denied P_TRACE from %d to %d by %d.\n",                          proc_selfpid(),                         proc_pid(targetProc),                         kauth_cred_getuid(credential)                     );                     *errPtr = EPERM;                     result = KAUTH_RESULT_DENY;                 }             }             break;         default:             // do nothing             break;     }      return result; }
```

__Note:__ Kauth is not invoked when a program is started by the debugger. You can detect this case using the technique shown in [Technical Q&A QA1361, 'Detecting the Debugger'](https://developer.apple.com/qa/qa2004/qa1361.html).

### Anti-Virus Scanner

Kauth allows you to implement an anti-virus program that supports both "on access" and "post modification" file scanning. The latter is easy: all you need to do is register a listener for the `KAUTH_SCOPE_FILEOP` scope and watch for the `KAUTH_FILEOP_CLOSE` action. If you see a modified file being closed, you can pass that file to your user space daemon for scanning. As the scanning proceeds asynchronously in the background, there should be no problems with deadlock.

Implementing "on access" scanning is more challenging. Your approach depends on whether you can always fix a file. If that's the case, you can listen for `KAUTH_FILEOP_OPEN` (in the `KAUTH_SCOPE_FILEOP`) and scan the file immediately after it's been opened. However, the result of your listener is always ignored, so there is no way to deny the actor access to that file.

If you can't always fix a file, and thus you may want to deny the actor access to the file, you must listen for the appropriate actions in the `KAUTH_SCOPE_VNODE` scope. If you scan a file, detect that it's infected, and can't fix it, you should return `KAUTH_RESULT_DENY` to prevent the actor from using it.

The difficulty with both of these "on access" approaches is avoiding deadlock. See Implementing a Listener for a detailed discussion of this problem.

### New Kernel Subsystem

If you're implementing an entirely new kernel subsystem (for example, a sophisticated protocol stack), you may decide to implement your authorization using Kauth. There are seven steps to this:

1. Decide on a scope name. You should use a reverse DNS-style name, as illustrated by the built-in scopes described in this document.
2. Decide on a set of actions. You can choose to use either an enumeration (as done by the file operations scope) or a bitmask (as used by the vnode scope).
3. For each action, you must decide what request-specific arguments (of type `arg0` through `arg3`) are appropriate for that action. It's easiest if the arguments are the same for all of the actions within your scope, but that's not required.
4. Write a default listener for your scope. This listener should be able to make authorization decisions based on:

   - the identity of the actor (as represented by the listener's `credentials` parameter)
   - the requested action
   - the request-specific arguments

   Your listener can extract information from the credentials using the accessor functions defined in <sys/kauth.h>.
5. Create your scope, and register your listener as the default listener, using `kauth_register_scope`.
6. Create a scope-specific wrapper function for `kauth_authorize_action` that:

   - supplies a reference to the scope created in the previous step
   - casts your scope-specific arguments to the generic arguments (`arg0` through `arg3`) used by `kauth_authorize_action`
7. Call your scope-specific wrapper function to authorize specific actions at appropriate places in your kernel subsystem.
[Back to Top](#)

## KauthORama Sample Code

[Sample Code 'KauthORama'](https://developer.apple.com/samplecode/KauthORama/index.html) is a great tool for exploring Kauth. It allows you to register a dummy listener for any scope. The listener always returns `KAUTH_RESULT_DEFER`, and so has no effect on authorization decisions, but it prints a record of the authorization request. Using this you can see how Kauth interacts with high-level operations, like listing directories or copying files. The sample's read me file has instructions for doing this.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-03-23 | A minor update to address some points of confusion. Firstly, KAUTH_PROCESS_CANSIGNAL is not implemented on any version of Mac OS X, not just Mac OS X 10.4 (r. 7724502). Secondly, the behaviour of kauth_authorize_fileop is non-obvious and this update clarifies its behavior (r. 5777071). Finally, there were some minor changes to account for the very small differences in Kauth since Mac OS X 10.4. |
| 2007-01-16 | Document a kernel bug that causes certain arguments to be NULL. |
| 2006-03-21 | Corrected problems with non-ASCII characters. |
| 2005-06-03 | New document that describes the kernel authorization (kauth) subsystem and its associated KPI. |

