---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/WhereToPutFiles.html
archived_at: '2026-07-15T08:15:35.747597Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](Files%20and%20the%20Finder.md)[Previous](The%20Developer%20Directory.md)

# Where to Put Application Files

Applications should be placed in the `/Applications` directory or the `~/Applications` directory of the current user. Applications placed in the `/Applications` directory are available to all users on the system. Applications placed in a user’s home directory are available only to that user.

All of the resources and data files required for an application to run should reside inside the application [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4). However, applications often come with extra files, such as templates, plug-ins, and other application extensions over which the user has some degree of control, including whether or not they should be installed. Similarly, an application might generate cache and temporary files that should not reside in the application bundle.

The remaining sections include some of the appropriate and inappropriate locations for application files. For information about the purpose and intended content of specific `Library` subdirectories, see [The Library Directory](The%20Library%20Directory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4delkciffeqq2ijjeq).

A support file is any type of file that supports the application but is not required for the application to run. Document templates and sample files are simple examples of support files. However, you might store more application-bound information, such as custom configurations or preset data files for your application’s workspace. In these instances, the information is intrinsically tied to a specific application (as opposed to the user’s data) but is not essential for the application to run.

The preferred location for nearly all support files is in the `Application Support` directory of the appropriate domain. Which domain you choose to store your support files depends on the intended use of those resources. If the resources apply to all users on the system, such as document templates, place them in `/Library/Application Support`. If the resources are user-specific, such as workspace configuration files, place them in the current user’s `~/Library/Application Support` directory.

Within the `Application Support` directory, you should always place support files in a custom subdirectory named for your application or company. Normally, you should use the application name, but you might want to use your company name if you have multiple products that share many of the same resources. How you organize the resources in this custom subdirectory is entirely up to you.

Even if a support file is user-specific, your application should not have any trouble accessing it from multiple user sessions. Because of fast user switching and remote logins, it’s possible that the same user could be logged into the computer more than once. Support files should not contain any data that would adversely affect the behavior of multiple user sessions. All sessions should see the exact same behavior.

Plug-ins are code bundles that extend the behavior of an application. Mac OS X supports several types of specialized plug-ins to handle contextual menus and Internet content among other things. You can also define a plug-in interface for your application that lets third-party developers extend the behavior of your application.

Mac OS X plug-ins typically reside in a subdirectory of the `Library` directory in either the local or system domain. User-specific versions of these plug-ins may reside in the user domain as well. See [The Library Directory](The%20Library%20Directory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4delkciffeqq2ijjeq) for a list of standard `Library` subdirectories.

The preferred location for application plug-ins is inside the application [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) itself. An application bundle can include a `PlugIns` directory for storing native and third-party plug-ins. Users can add plug-ins to this directory using the Get Info window of the Finder. Third-party plug-in developers can also install the plug-ins automatically using an installer package. If your application shares a set of plug-ins with another application, you may also install plug-ins in your custom subdirectory of `Library/Application Support`.

When deciding where to store plug-ins, be sure to consider licensing issues and the intended user experience. Plug-ins stored inside the application bundle always remain with the application. If the user copies the application to a different volume, the application retains any installed plug-ins. However, if you install plug-ins in a `Library/Application Support` subdirectory, those plug-ins may be limited to specific users booting from a specific disk partition.

Many applications use temporary files to store transient data. The life span of a temporary file varies depending on its intended use. The file may be used to store scratch data or calculations, such as when rendering a 3D image, and deleted immediately upon completion of those calculations. It may store runtime data about the application and be deleted only when the application terminates. It may also linger until the next time the user launches the application. For example, an application typically uses a temporary file to store an autosave version a document, which acts like an insurance policy against application or system crashes.

Mac OS X provides an established set of directories for storing temporary files. The primary directory (`/tmp`) is where most local files go, but you should never hardcode this path into your application. Using hardcoded paths limits the portability and longevity of your code. Instead, Carbon applications should use the `FSFindFolder` function (in the Core Services framework) to obtain a reference to the temporary directory; Cocoa applications should use the `NSTemporaryDirectory` function in Foundation Kit.

When saving temporary files, make sure you use unique filenames. Running applications typically share the same temporary directory. With fast user switching enabled, several instances of the same application might also share this directory. Each instance of your application should easily be able to identify the files it created. You can incorporate the session ID and application name into your temporary file names directory or use that information to identify a subdirectory containing your temporary files. For more information about session IDs and operating safely with fast user switching, see _[Multiple User Environment Programming Topics](../Multiple%20User%20Environment%20Programming%20Topics/Introduction%20to%20Multiple%20User%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4da2i)_ in Mac OS X Documentation.

A cache file is a special type of file generally used to improve the performance of your application. You can use cache files in situations where retrieving or recreating the data might be an expensive operation. For example, web browsers cache previously visited web pages to improve the load time for that page later, assuming its content hasn’t changed.

Cache files should be placed in a custom subdirectory of `~/Library/Caches` in nearly all cases. The name of the custom subdirectory should match the bundle identifier of your application. Because they are typically specific to a single user session, you should also tag your cache files, or their contents, with the session ID of the current user. For information on how to do this, see _[Multiple User Environment Programming Topics](../Multiple%20User%20Environment%20Programming%20Topics/Introduction%20to%20Multiple%20User%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4da2i)_ in Mac OS X Documentation.

If you have cache files that are relevant to all users of the application, you can store them in the local domain (`/Library/Caches`) instead of the user domain (`~/Library/Caches`).

It is important to remember that the user domain (`/Users`) is intended for files created by the user. With the exception of the `~/Library` directory, your application should never install files into the user’s home directory. In particular, you should never install files into a user’s `Documents` directory or into the `/Users/Shared` directory. These directories should only be modified by the user.

Even if your application provides clip art or sample files that the user would normally manipulate, you should place those files in either the local or user’s `Library/Application Support` directory by default. The user can move or copy files from this directory as desired. If you are concerned about the user finding these files, you should include a way for the user to browse or access them directly from your application’s user interface.

[Next](Files%20and%20the%20Finder.md)[Previous](The%20Developer%20Directory.md)

