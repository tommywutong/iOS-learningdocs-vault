---
title: Authorization Services Programming Guide
apple_id: TP30000995
resource_type: Guide
platform: macOS
topic: Security
technology: Security
published: '2011-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/03authtasks/authtasks.html
archived_at: '2026-07-18T02:06:40.546545Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Authorization Services Programming Guide](Introduction%20to%20Authorization%20Services%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Authorization%20Concepts.md)

# Authorization Services Tasks

This chapter provides instructions and code samples for tasks you can accomplish with Authorization Services. You can adapt these samples in your own application to

- Restrict access to parts of your own application
- Call system utilities
- Edit privileged files
- Install your privileged tools

A simple, self-restricting application needs to restrict a user from the application’s own operations with minimal security concerns—for example, a grades-and-transcripts application might only allow the registrar to create transcripts. Read [Authorizing in a Simple, Self-Restricted Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2ji5cuqrcj) if you have a self-restricting application.

If you have a factored application—for example, an application that must perform an operation as root, such as restarting a daemon—you should read both [Authorizing in a Simple, Self-Restricted Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2ji5cuqrcj) and [Authorizing in a Factored Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2ji5ausqkh).

If your installer must perform a privileged operation, read [Calling a Privileged Installer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummzt) to see an example of an installer using Authorization Services.

See Sample Code > Security for sample applications that perform system-restricted privileged operations.

A simple, self-restricted application uses Authorization Services to perform the tasks described in the following sections:

- [Creating an Authorization Reference Without Rights](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdjbbukrkh)
- [Requesting Authorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdijcemqsc)
- [Releasing an Authorization Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdizeeoqsi)

The Security Server uses the authorization reference to access the state of the authorization session, which includes any stored credentials. Your application needs only one authorization reference.

You use the [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate) function to allocate memory for the authorization reference. The code fragment in Listing 2-1 shows a call to the `AuthorizationCreate` function that creates an authorization reference without rights. An authorization reference without rights is useful if the rights are not needed immediately, but the authorization reference is required so it can be used in different parts of the application. For example, in the grades-and-transcripts application, the authorization reference might be created when the application starts, but rights aren’t requested until the user attempts to create transcripts.

__Listing 2-1__  Creating an authorization reference without rights

```
AuthorizationRef myAuthorizationRef;
OSStatus myStatus;
myStatus = AuthorizationCreate (NULL, kAuthorizationEmptyEnvironment,
            kAuthorizationFlagDefaults, &myAuthorizationRef);
```

The [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate) function takes four parameters. The first is an authorization rights set. Since `NULL` is passed, no rights are authorized at this time. The second parameter is the authorization environment, which is not currently implemented; pass [kAuthorizationEmptyEnvironment](https://developer.apple.com/documentation/security/kauthorizationemptyenvironment). The third parameter is the authorization options. The constant [kAuthorizationFlagDefaults](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagdefaults) is passed because the application is not requesting any rights. The fourth parameter is the address of the authorization reference you declared. On return, the authorization reference refers to the current authorization session. If the authorization reference is created successfully, the function returns [errAuthorizationSuccess](https://developer.apple.com/documentation/security/1540004-authorization_services_result_co/errauthorizationsuccess).

[Requesting Authorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdijcemqsc) describes how to use the [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) and [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate) functions to request authorization. When your application is done with the authorization reference, use the [AuthorizationFree](https://developer.apple.com/documentation/security/1394257-authorizationfree) function as described in [Releasing an Authorization Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdizeeoqsi).

After you create an authorization reference, you can then request authorization. Your application should perform authorization immediately before every privileged operation. In the case of the grades-and-transcripts example, the application requests authorization immediately before creating a transcript.

When your application requests authorization, the Security Server may request the user to authenticate. Authorization Services allows you to take full advantage of the Security Server’s authentication plug-in architecture to deal with authentication for you. Instead of a user name and password, the authentication may use fingerprints or smart cards, but your application code stays the same.

[Figure 1-3](Authorization%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqguwueqkkjbaugskg) shows the authentication dialog that the Security Server provides. The user enters an administrator user name and password and clicks OK. The Security Server then uses the user name and password to authenticate and authorize the user.

Authorization requires the creation of an authorization rights set and authorization options to use in a call to the functions [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) or [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate). In your application, request authorization by performing the tasks described in the following sections:

- [Creating an Authorization Rights Set](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjr)
- [Specifying Authorization Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdiveugqkj)
- [Authorizing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjs)
- [Releasing an Authorization Item Array](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjt)

To authorize a user for specific rights, you must create an authorization rights set to pass to the Security Server through the [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) or [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate) functions. The authorization rights set consists of an authorization item array and the number of items in the authorization item array. The authorization item array contains information about the rights that your application is requesting.

Each item in the authorization item array consists of four pieces of information:

- The name of the right
- A value that contains optional data pertaining to the right
- The byte length of the `value` field
- Optional flags

Listing 2-2 shows an example of an authorization item array. In most cases, when creating an item for a right, you set the `value` field to `NULL`, and the `valuelength` and `flags` fields to `0`. You should set the `name` field to the name of the right you are requesting. For information on naming your own rights, see [Rights](Authorization%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqguwviucykjcummjw).

__Listing 2-2__  Creating an authorization item array

```
AuthorizationItem myItems[2];

myItems[0].name = "com.myOrganization.myProduct.myRight1";
myItems[0].valueLength = 0;
myItems[0].value = NULL;
myItems[0].flags = 0;

myItems[1].name = "com.myOrganization.myProduct.myRight2";
myItems[1].valueLength = 0;
myItems[1].value = NULL;
myItems[1].flags = 0;
```

For example, a grades-and-transcripts application might request the right `com.myOrganization.myProduct.transcripts.create`. The `valueLength`, `value`, and `flags` fields would be unused and set to `0`, `NULL`, and 0, respectively.

Listing 2-3 shows an example of an authorization rights set. In the authorization rights set, the `count` field contains the number of rights in the authorization item array, while the `items` field points to the authorization item array you created.

__Listing 2-3__  Creating a set of authorization rights

```
AuthorizationRights myRights;
myRights.count = sizeof (myItems) / sizeof (myItems[0]);
myRights.items = myItems;
```


You use the authorization options to instruct the Security Server how to proceed with the [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) and [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate) functions. By setting the authorization options, you can use these functions to

- Authorize partial rights
- Authorize all rights
- Preauthorize rights

You can include with these options the option to interact with the user. The Security Server requires user interaction to perform authentication. The most common combination authorizes all rights and allows user interaction. Listing 2-4 shows an example of the authorization options for authorization.

__Listing 2-4__  Specifying authorization options for authorization

```
AuthorizationFlags myFlags;
myFlags = kAuthorizationFlagDefaults |
            kAuthorizationFlagInteractionAllowed |
            kAuthorizationFlagExtendRights;
```

The [kAuthorizationFlagDefaults](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagdefaults) constant zeros the bit mask. The [kAuthorizationFlagExtendRights](https://developer.apple.com/documentation/security/authorizationflags/1400419-extendrights) constant instructs the Security Server to grant the rights. Without this flag, the [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) and [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate) functions would return the appropriate error code, but no rights would be extended to the user.

If your application does not require all of the rights to be authorized, you can include the [kAuthorizationFlagPartialRights](https://developer.apple.com/documentation/security/authorizationflags/1394760-partialrights) constant to request partial authorization. You can then determine what to allow the user to do based on which rights the Security Server grants. Listing 2-5 shows an example of setting the authorization options for partial authorization.

__Listing 2-5__  Specifying authorization options for partial authorization

```
myFlags = kAuthorizationFlagDefaults |
            kAuthorizationFlagInteractionAllowed |
            kAuthorizationFlagExtendRights |
            kAuthorizationFlagPartialRights;
```

See [Requesting Preauthorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2jivdumske) to learn what authorization options to set for preauthorization.

The code fragment in Listing 2-6 shows a call to the [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) function based on the authorization reference and authorization rights set you created and the authorization options you specified. In the grades-and-transcripts example, the `AuthorizationCopyRights` function is used to authorize the right to create a transcript.

__Listing 2-6__  Authorizing rights

```
myStatus = AuthorizationCopyRights (myAuthorizationRef, &myRights,
        kAuthorizationEmptyEnvironment, myFlags, NULL);
```

The first parameter is the authorization reference created in [Creating an Authorization Reference Without Rights](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdjbbukrkh). The second parameter is the authorization rights set created in [Creating an Authorization Rights Set](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjr). The third parameter is the authorization environment. The authorization environment is not currently implemented, so pass [kAuthorizationEmptyEnvironment](https://developer.apple.com/documentation/security/kauthorizationemptyenvironment). The fourth parameter is the authorization options set in [Specifying Authorization Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdiveugqkj).

The fifth parameter is useful when authorizing partial rights as shown in Listing 2-7. This parameter points to an empty authorized rights set you declare. On return, this consists of the rights that the Security Server actually authorizes. If you create a pointer to an authorized rights set, then you should release it as described in [Releasing an Authorization Item Array](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjt).

__Listing 2-7__  Authorizing partial rights

```
AuthorizationRights *myAuthorizedRights;
myStatus = AuthorizationCopyRights (myAuthorizationRef, &myRights,
            kAuthorizationEmptyEnvironment, myFlags,
            &myAuthorizedRights);
```

The [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) function returns [errAuthorizationSuccess](https://developer.apple.com/documentation/security/1540004-authorization_services_result_co/errauthorizationsuccess) if the Security Server grants all the rights. You can use the return status to determine whether the user may perform the privileged operation.

You can use an authorization rights set and authorization options to request authorization when you create an authorization reference.

Listing 2-8 shows an example combining authorization with the [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate) function.

__Listing 2-8__  Creating an authorization reference with rights

```
myStatus = AuthorizationCreate (&myRights, kAuthorizationEmptyEnvironment,
            myFlags, &myAuthorizationRef);
```

You can also use the [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate) function to authorize a user for a one-time privileged operation. One-time authorization is useful if your application needs to authorize only once when it is run. Listing 2-9 shows an example of how to use an authorization rights set and authorization options with the `AuthorizationCreate` function without producing an authorization reference. Pass `NULL` instead of an authorization reference.

__Listing 2-9__  A one-time authorization call

```
myStatus = AuthorizationCreate (&myRights, kAuthorizationEmptyEnvironment,
            myFlags, NULL);
```


When you finish with the authorization item set in [Listing 2-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2ji5buoq2e), call the [AuthorizationFreeItemSet](https://developer.apple.com/documentation/security/1392929-authorizationfreeitemset) function, as shown in Listing 2-10, to release the memory it uses. Use this function only on authorization item arrays that the Security Server allocates, such as those used in the [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) and [AuthorizationCopyInfo](https://developer.apple.com/documentation/security/1397734-authorizationcopyinfo) functions.

__Listing 2-10__  Releasing an authorization item array

```
myStatus = AuthorizationFreeItemSet (myAuthorizedRights);
```


Before exiting your application, or at any time you want to end the current authorization session, call the [AuthorizationFree](https://developer.apple.com/documentation/security/1394257-authorizationfree) function to release the authorization reference. For example, the grades-and-transcripts application would wait until the user quits the application before releasing the authorization reference. Using the same authorization reference every time the user creates a transcript allows the Security Server to reuse any shared credentials that haven’t expired. In contrast, an action such as the user clicking the open-lock button in the Network preferences pane can trigger the release of the authorization reference, requiring the user to reauthorize when she clicks the closed-lock button.

The code segment in Listing 2-11 shows an example of using the [AuthorizationFree](https://developer.apple.com/documentation/security/1394257-authorizationfree) function. You must pass the authorization reference and authorization options. For authorization options, pass the constant [kAuthorizationFlagDefaults](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagdefaults) if you want to revoke the credentials associated with the current process, or pass the constant [kAuthorizationFlagDestroyRights](https://developer.apple.com/documentation/security/authorizationflags/1397545-destroyrights) to release all shared credentials from all processes that use them.

__Listing 2-11__  Releasing an authorization reference

```
myStatus = AuthorizationFree (myAuthorizationRef,
            kAuthorizationFlagDestroyRights);
```


Factored applications, whether system-restricted or self-restricted, use an application to control the graphical user interface and nonprivileged operations and use a separate helper tool to perform the privileged operations.

Read [Using Authorization Services in a Factored Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummzv) for a description of using Authorization Services in a factored application and [Using Authorization Services in a Helper Tool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummzw) for a description of using Authorization Services in a helper tool.

You can use Authorization Services in your factored application to perform the tasks described in the following sections:

- [Creating an Authorization Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2ji5feeskj)
- [Requesting Preauthorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2jivdumske)
- [Creating an External Authorization Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummju)
- [Calling a Helper Tool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummry)
- [Releasing an Authorization Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2jjjduescg)

An example of a factored application is one that restarts the Internet daemon. The application performs all the nonprivileged operations while the helper tool restarts the daemon. The application creates an authorization reference and preauthorizes the right to restart the Internet daemon. The application uses the result to determine whether to start the helper tool. The application creates an external version of the authorization reference and passes it to the helper tool. When the authorization reference is no longer needed, the application releases it.

Creating an authorization reference in a factored application is the same as in a simple, self-restricting application. See [Creating an Authorization Reference Without Rights](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdjbbukrkh) to learn how to create an authorization reference.

You should preauthorize rights before calling a helper tool. Using the results of preauthorization, you can prevent an unauthorized user from invoking the helper tool. Doing so saves the time of starting a new process and using resources as well as saving the user from preparing to perform an operation he doesn’t have privileges to perform.

Preauthorization requires the creation of an authorization rights set and authorization options to use in a call to the functions [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) or [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate). In your application, you preauthorize a user by performing the steps described in the following sections:

- [Creating a Preauthorization Rights Set](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdjbdekrse)
- [Specifying Authorization Options for Preauthorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcumoi)
- [Preauthorizing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2ji5duorkh)

A preauthorization rights set is the same as an authorization rights set as described in [Creating an Authorization Rights Set](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjr).

Authorization options for preauthorization are similar to the authorization options for authorization and partial authorization described in [Specifying Authorization Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdiveugqkj). The only difference between preauthorization and authorization is that you are not using the result to determine if a user can perform a privileged operation. Instead, you should use the result to determine if the user can be authorized at a later time.

Listing 2-12 shows an example of setting the authorization options for preauthorization. The [kAuthorizationFlagDefaults](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagdefaults) constant zeros out the bit mask. The [kAuthorizationFlagExtendRights](https://developer.apple.com/documentation/security/authorizationflags/1400419-extendrights) constant tells the Security Server to extend any rights granted to the user. The [kAuthorizationFlagInteractionAllowed](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflaginteractionallowed) constant tells the Security Server that it may interact with the user for authentication purposes. The [kAuthorizationFlagPreAuthorize](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagpreauthorize) constant tells the Security Server to preauthorize the rights requested.

__Listing 2-12__  Specifying authorization options for preauthorization

```
AuthorizationFlags myFlags;
myFlags = kAuthorizationFlagDefaults |
            kAuthorizationFlagExtendRights |
            kAuthorizationFlagInteractionAllowed |
            kAuthorizationFlagPreAuthorize;
```


Calling the [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) or [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate) function is the same for preauthorization as it is for authorization. See [Listing 2-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummzx) in the section [Authorizing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjs) for examples.

After creating the authorization reference and preauthorizing rights, you need to pass the authorization reference to your helper tool. Sharing the authorization reference allows the helper tool to use any credentials that are part of the factored application’s authorization session. When you pass the authorization reference to your helper tool, the authorization dialog can show your application’s path rather than the path to the helper tool. It also enables the system to determine whether the authorization dialog should have keyboard focus.

One problem with the authorization reference is that it is not in a form that can be transferred from one process to another. To solve this problem, Authorization Services provides a function to translate the authorization reference into an external authorization reference that you can pass to your helper tool.

To create an external authorization reference, declare a variable of type `AuthorizationExternalForm` and pass it to the [AuthorizationMakeExternalForm](https://developer.apple.com/documentation/security/1397335-authorizationmakeexternalform) function along with the existing authorization reference. On return, that variable contains a transferable form of the authorization reference. Listing 2-13 shows an example of creating an external authorization reference.

__Listing 2-13__  Creating an external authorization reference

```
AuthorizationExternalForm myExternalAuthorizationRef;
myStatus = AuthorizationMakeExternalForm (myAuthorizationRef,
            &myExternalAuthorizationRef);
```

Read `[“Retrieving an Authorization Reference”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjw)` to learn how to retrieve the authorization reference from the external authorization reference in your helper tool.

When you are ready to call your helper tool, pass the external authorization reference to the tool using some form of interprocess communication, such as a communications pipe.

Releasing the authorization reference in a factored application is the same as described in [Releasing an Authorization Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdizeeoqsi).

You can use Authorization Services in your helper tool to perform the tasks described in the following sections:

- [Retrieving an Authorization Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjw)
- [Performing Authorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2jiraugr2j)
- [Executing the Privileged Operation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2jincuursc)

For example, a helper tool that restarts the Internet daemon retrieves the authorization reference from the external authorization reference passed by the application. Then the helper tool requests authorization immediately before restarting the Internet daemon.

If your helper tool is actually a self-repairing helper tool, you should also read [Repairing a Helper Tool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummrz).

To share the authorization session, the factored application passes an external authorization reference to the helper tool (see [Creating an External Authorization Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummju)). In the helper tool, you use the [AuthorizationCreateFromExternalForm](https://developer.apple.com/documentation/security/1400640-authorizationcreatefromexternalf) function to retrieve an authorization reference from the external authorization reference.

Listing 2-14 shows an example using the `AuthorizationCreateFromExternalForm` function. In this example, the external authorization reference is read in from a communications pipe between the helper tool process and the parent process. You then pass the external authorization reference to the function `AuthorizationCreateFromExternalForm`. On return, `myAuthorizationRef` is the authorization reference.

__Listing 2-14__  Retrieving an authorization reference

```
AuthorizationRef myAuthorizationRef;
AuthorizationExternalForm myExternalAuthorizationRef;
OSStatus myStatus;

/* *** You should read in the external authorization reference into
        myExternalAuthorizationRef here. *** */

myStatus = AuthorizationCreateFromExternalForm (&myExternalAuthorizationRef,
            &myAuthorizationRef);
```


Performing authorization in your helper tool is the same as it is for simple, self-restricted applications. See [Requesting Authorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdijcemqsc) for more information.

You should use the result of the authorization to determine whether the user is allowed to perform the privileged operation. There are no Authorization Services functions required for actually executing the privileged operation.

If your helper tool needs to run as root to perform privileged operations, such as restarting the Internet daemon, then it should have its setuid bit set. Tools that have the setuid bit set (sometimes referred to as _setuid tools_) must be Mach-O binaries because CFM binaries don’t support the setuid or setgid (set group identifier) bit. When you install your program, your installer should set the helper tool’s setuid bit, and set its owner to root.

In OS X 10.1 and earlier, when a user moves a setuid tool to another volume, or copies it from one place to another, the setuid bit is reset by the file system and the group and owner change to match the user moving the setuid tool. This is done purposely to reduce the security risk that a setuid tool poses by allowing any user to run the setuid tool as root. On the other hand, most users expect that when they copy an application or tool from one folder to another, it will still work. Thus, the setuid bit, group, and owner need to be reset without editing the permissions in the terminal window. This section provides code to allow your setuid tool to repair its own setuid bit when this problem occurs.

All setuid tools are potential security problems. This case poses a particular problem because the tool self-repairs its setuid bit even if a user tampers with the setuid tool’s code. As added security, you might want to display a warning to users whenever performing this action so they can decide to continue or cancel the self-repair operation, or possibly force the user to reinstall the application from the installer.

You can repair the setuid bit on your helper tool by performing the tasks described in the following sections:

- [Calling a Helper Tool as Root](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjy)
- [Setting the Setuid Bit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2jjfcuqssc)

For your helper tool to set its own setuid bit, the tool must have root privileges. This is a circular problem, since you can’t change permissions on your helper tool unless your helper tool is already running as root. This is where the function [AuthorizationExecuteWithPrivileges](https://developer.apple.com/documentation/security/1540038-authorizationexecutewithprivileg) comes into play.

The `AuthorizationExecuteWithPrivileges` function executes any application as root through a special security process. The code sample in Listing 2-15 demonstrates how a helper tool can recursively call itself with root privileges so it can repair its own setuid bit.

__Listing 2-15__  Executing a helper tool with root privileges

```
FILE *myCommunicationsPipe = NULL;
char *myArguments[] = {"--self-repair", NULL};
char myPath[MAXPATHLEN];

/* *** You should determine the path of your tool here and put the result in
        myPath. *** */

myStatus = AuthorizationExecuteWithPrivileges (myAuthorizationRef,
            myPath, kAuthorizationFlagDefaults, myArguments,
            &myCommunicationsPipe);
```

The [AuthorizationExecuteWithPrivileges](https://developer.apple.com/documentation/security/1540038-authorizationexecutewithprivileg) function expects you to pass five parameters. The first parameter is the authorization reference you retrieved as shown in [Retrieving an Authorization Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjw). The authorization reference allows the helper tool to use any credentials that are part of the factored application’s authorization session. The second parameter is the full POSIX pathname of the helper tool—in this case, the setuid tool—that is being called. The third parameter is the authorization options. In this function, this parameter is not implemented, so for now, set it to [kAuthorizationFlagDefaults](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagdefaults). The fourth parameter is a null-terminated array of arguments for the tool being called. You can use this parameter to pass any information you need from the parent process to the child process. In this case, the string `"--self-repair"` is passed to indicate to the helper tool that it should execute the code in [Listing 2-16](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueq2jivfeqscf). The fifth parameter is a communications pipe so the helper tool can pass the data it received from the factored application to itself.

In [Listing 2-15](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummrw), the helper tool recursively calls itself, passing the self-repair argument, `--self-repair`. Therefore, in the same helper tool, you need to check for the self-repair argument and, if it is found, fix the setuid bit. See the More Is Better sample code (_[MoreIsBetter](../../../samplecode/MoreIsBetter/MoreIsBetter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanztgi)_) for a sample self-repairing setuid tool.

When you call the `AuthorizationExecuteWithPrivileges` function, you need a way to retrieve the authorization reference that is passed in the call. Listing 2-16 shows code using the [AuthorizationCopyPrivilegedReference](https://developer.apple.com/documentation/security/1540021-authorizationcopyprivilegedrefer) function to retrieve the authorization reference. The only time you use this function is to retrieve an authorization reference passed by a call to `AuthorizationExecuteWithPrivileges`.

The first parameter of the call to the `AuthorizationCopyPrivilegedReference` function is an empty authorization reference you declare. You should not call the [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate) function. On return, the authorization reference points to a copy of the original authorization reference. The second parameter is not implemented, so set it to [kAuthorizationFlagDefaults](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagdefaults).

__Listing 2-16__  Setting the setuid bit

```
myStatus = AuthorizationCopyPrivilegedReference (&myAuthorizationRef,
            kAuthorizationFlagDefaults)
```


Occasionally, an installer must install files in directories that are not owned by the user running the installer. This should be a rare case and you should avoid it if at all possible. In the event that it can’t be avoided, the code in Listing 2-17 shows a tool that runs the `/usr/bin/id` utility with optional flag `-un`. By replacing the utility path and including your own flags, you can use this sample code to call your installer with root privileges. Your installer will then be able to perform any privileged operations it requires.

__Listing 2-17__  Calling a privileged installer

```c
#include <Security/Authorization.h>
#include <Security/AuthorizationTags.h>

int read (long,StringPtr,int);
int write (long,StringPtr,int);

int main() {

    OSStatus myStatus;
    AuthorizationFlags myFlags = kAuthorizationFlagDefaults;              // 1
    AuthorizationRef myAuthorizationRef;                                  // 2

    myStatus = AuthorizationCreate(NULL, kAuthorizationEmptyEnvironment,  // 3
                myFlags, &myAuthorizationRef);
    if (myStatus != errAuthorizationSuccess)
        return myStatus;

    {
        AuthorizationItem myItems = {kAuthorizationRightExecute, 0,    // 4
                NULL, 0};
        AuthorizationRights myRights = {1, &myItems};                  // 5

        myFlags = kAuthorizationFlagDefaults |                         // 6
                kAuthorizationFlagInteractionAllowed |
                kAuthorizationFlagPreAuthorize |
                kAuthorizationFlagExtendRights;
        myStatus = AuthorizationCopyRights (myAuthorizationRef,        // 7
                                     &myRights, NULL, myFlags, NULL );
    }

    if (myStatus != errAuthorizationSuccess) goto DoneWorking;

    {
        char myToolPath[] = "/usr/bin/id";
        char *myArguments[] = { "-un", NULL };
        FILE *myCommunicationsPipe = NULL;
        char myReadBuffer[128];

        myFlags = kAuthorizationFlagDefaults;                          // 8
        myStatus = AuthorizationExecuteWithPrivileges                  // 9
                (myAuthorizationRef, myToolPath, myFlags, myArguments,
                &myCommunicationsPipe);

        if (myStatus == errAuthorizationSuccess)
            for(;;)
            {
                int bytesRead = read (fileno (myCommunicationsPipe),
                        myReadBuffer, sizeof (myReadBuffer));
                if (bytesRead < 1) goto DoneWorking;
                write (fileno (stdout), myReadBuffer, bytesRead);
            }
    }

    DoneWorking:

    AuthorizationFree (myAuthorizationRef, kAuthorizationFlagDefaults); // 10

    if (myStatus) printf("Status: %ld\n", myStatus);
    return myStatus;
}
```

Here are explanations of the numbered lines of code in Listing 2-17:

1. Declare a variable to store authorization options.
2. Declare an authorization reference.
3. Use the [AuthorizationCreate](https://developer.apple.com/documentation/security/1397453-authorizationcreate) function to initialize the authorization reference. See [Creating an Authorization Reference Without Rights](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdjbbukrkh) for more information.
4. Create an authorization item array. The user must have the right to execute to use the [AuthorizationExecuteWithPrivileges](https://developer.apple.com/documentation/security/1540038-authorizationexecutewithprivileg) function. To create a right to execute authorization item, set the `name` field to [kAuthorizationRightExecute](https://developer.apple.com/documentation/security/kauthorizationrightexecute), the `value` fields to `NULL`, the `valueLength` and `flags` fields to `0`. See [Creating an Authorization Rights Set](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjr) for more information.
5. Create an authorization rights set. Set the `count` field to the number of items in the authorization item array, and set the `items` field to point to the authorization item array. See [Creating an Authorization Rights Set](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjr) for more information.
6. Set the authorization options to preauthorize the rights. See [Specifying Authorization Options for Preauthorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcumoi) for more information.
7. Use the [AuthorizationCopyRights](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights) function to preauthorize the right to execute your installer as root. In this case, there is no reason to continue if the user can’t preauthorize. See [Authorizing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjs) for more information.
8. Set the authorization options for the [AuthorizationExecuteWithPrivileges](https://developer.apple.com/documentation/security/1540038-authorizationexecutewithprivileg) function to [kAuthorizationFlagDefaults](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagdefaults). Other authorization options, such as that specified by the [kAuthorizationFlagInteractionAllowed](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflaginteractionallowed) constant, are not necessary because the `AuthorizationExecuteWithPrivileges` function interacts with the user whether you specify the option or not.
9. Use the `AuthorizationExecuteWithPrivileges` function to invoke your installer. Pass the authorization reference in the first parameter. Pass the installer’s full POSIX pathname in the second parameter. Pass the authorization options default in the third parameter. Pass any arguments for the installer in the fourth parameter. A communications pipe to the tool may be set up through the fifth parameter. See [Calling a Helper Tool as Root](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviucykjcummjy) for more information about the `AuthorizationExecuteWithPrivileges` function.
10. Release the authorization reference using the [AuthorizationFree](https://developer.apple.com/documentation/security/1394257-authorizationfree) function. See [Releasing an Authorization Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywueqsdizeeoqsi) for more details.

[Next](Document%20Revision%20History.md)[Previous](Authorization%20Concepts.md)

