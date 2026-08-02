---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/Domains.html
archived_at: '2026-07-15T08:15:26.127966Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](The%20Library%20Directory.md)[Previous](Introduction%20to%20the%20File%20System%20Overview.md)

# File-System Domains

On a multi-user system, controlling access to system resources is important for maintaining the stability of the system. Mac OS X defines several file-system domains, each of which provides storage for resources in an established set of directories. Access to resources in each domain is determined by the permissions for the current user.

There are four file-system domains:

- 

  _User_. The user domain contains resources specific to the user who is logged in to the system. This domain is defined by the user’s home directory, which can either be on the boot volume (`/Users`) or on a network volume. The user has complete control of what goes into this domain.
- 

  _Local_. The local domain contains resources such as applications and documents that are shared among all users of a particular system but are not needed for the system to run. The local domain does not correspond to a single physical directory, but instead consists of several directories on the local boot (and root) volume. Users with system administrator privileges can add, remove, and modify items in this domain.
- 

  _Network_. The network domain contains resources such as applications and documents that are shared among all users of a local area network. Items in this domain are typically located on network file servers and are under the control of a network administrator.
- 

  _System_. The system domain contains the system software installed by Apple. The resources in the system domain are required by the system to run. Items in this domain are located on the local boot (and root) volume. Users cannot add, remove, or alter items in this domain.

The domain for a given resource determines its applicability or accessibility to the users of the system. For example, a font installed in the user’s home directory is available only to that user. If an administrator installs the same font in the network domain, all network users have access to it.

Within each domain, Mac OS X provides a set of initial directories for organizing the contained resources. Mac OS X uses identical directory names across domains to store the same types of resources. This consistency simplifies the process of finding resources both for the user and for the system methods that use those resources. When the system needs to find a resource, it searches the domains sequentially until it finds the resource. Searches start in the user domain and proceed through the local, network, and system domains in that order.

Your code should never assume the path to a resource within a file-system domain, as those paths could change in the future. Apple provides public interfaces for accessing standard file-system paths. You should always use these interfaces to locate system resources. See [Searching Within the File-System Domains](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dcljrgaytkojr) for more on searching for items within the domains.

The following sections describe the file-system domains in more detail, including some of the standard directories available in each domain.

The user domain contains resources that are specific to a single user. The user domain is represented by the home directory of the current (logged-in) user. Each user of a Mac OS X computer must have an account on that computer or on the local area network to which the computer is connected. Each user account comes with an assigned area of space in the file system, called the user’s home directory. This directory is where the user’s programs, resources, and documents reside. The name of each user’s home directory is based on the user’s short login name, which must be unique.

The user domain makes a customized working environment possible for each user. When a user logs in, the Finder restores the user’s working environment and settings to their previous state using the preferences in the user domain. Similarly, programs and other system software use information in the user domain to restore application preferences, network settings, email settings, font sets, ColorSync profiles, and other settings.

The location of the user’s home directory depends on the user account. If the user account is local to the computer, the user’s home directory is in the `Users` directory on the boot volume. If the user account is a network account, the home directory is on a network server. Regardless of the physical location of the home directory, Mac OS X uses the UNIX convention of a `~` (tilde) character in some situations to indicate a user’s home directory. The tilde character can be used in combination with other directory names or user names to specify specific user directories. [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dcljrgaytanzyfvbecsseiffeoqy) illustrates this concept.

__Table 1__  Uses of tilde to indicate locations in home directories

| `~` | Top level of current user’s home directory |
| `~/Library/Fonts` | Where fonts are stored in current user’s home directory |
| `~Steve` | Top level of user Steve’s home directory |

The home directory for each new user comes with some default directories and resources in place. If the user has a .Mac account, these directories are mirrored on the user’s iDisk as well. (For more information on iDisk, go to [http://www.mac.com](http://www.mac.com/).) [Table 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dcljrgaytcmzvfvbegskjivfeiqy) lists some of the common directories you might find in a user’s home directory.

__Table 2__  Home directory contents

| User directory | Description |
| `Applications` | Contains applications available only to the current user. |
| `Desktop` | Contains the items the Finder displays on the desktop for the logged-in user. |
| `Documents` | Contains the user’s personal documents. |
| `Library` | Contains application settings, preferences, and other system resources that are specific to the user. Should not contain user data. See [The Library Directory](The%20Library%20Directory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4delkciffeqq2ijjeq). |
| `Movies` | Contains digital movies in QuickTime and other formats. |
| `Music` | Contains digital music files (`.aiff`, `.mp3`, `.m4p`, and other formats). |
| `Pictures` | Contains image files in a variety of formats. |
| `Public` | Contains items the user wishes to share with other users. By default, this directory is accessible to other users. |
| `Sites` | Contains web pages for the user’s personal website. Web Sharing must be enabled before these pages are accessible to other users. |

When a user account is created, an `Applications` directory is not automatically added to the home directory. However, users can create an `Applications` directory and put their own applications in it. The system automatically searches for applications in this location.

The system protects the files and directories in the user’s home directory from outside interference by a set of default permissions, which the user may change at any time. Any new folders created by the user inherit the privileges of the parent directory. 

In addition to the individual home directories, the `Users` directory contains a `Shared` subdirectory. This directory is accessible to any user of the local computer system and is intended for use only by users; applications should not store application-specific content here, unless explicitly directed to do so by the user. Any user can write documents to, retrieve documents from, and read documents in this directory. Although this directory is not really associated with the user domain, it provides a convenient means for users to exchange documents and other files. 

The local domain contains resources that are available on the local computer but are not required by the system to run. Resources in the local domain typically include applications, utilities, custom fonts, custom startup items, and global application settings. The `Applications` and `Library` directories on the root volume contain the resources for the local domain. These resources are available to the current user of a computer system but are not available to users on other networked computers.

Administrators of a computer can install resources into the local domain if they want those resources to be shared by all users of the system. Apple ships its applications in the `/Applications` and `/Applications/Utilities` directories. Third-party applications and utilities should also be placed in these directories. Other system resources, such as fonts, ColorSync profiles, preferences, and plug-ins should be placed in the appropriate subdirectory of the `Library` directory. For more on the `Library` directory, see [The Library Directory](The%20Library%20Directory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4delkciffeqq2ijjeq).

The network domain contains the resources available to all users of a local area network. Network users can access applications, documents and other resources through this domain, including AppleShare and web servers. The exact composition of the network domain depends on institutional or corporate policy. Implementation of the network domain is the responsibility of the network administrator.

[Table 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dcljrgaytgnrufvbegskdjfduqrq) lists the standard directories available in the network domain, along with a description of the directory contents.

__Table 3__  Network directories

| Location | Description |
| `/Network/Applications` | Contains applications that can be run by all users on the local area network. |
| `/Network/Library` | Contains resources—such as plug-ins, sound files, documentation, frameworks, colors, and fonts—available to all users of a local area network. For more on the `Library` directory, see [The Library Directory](The%20Library%20Directory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4delkciffeqq2ijjeq). |
| `/Network/Servers` | Contains the mount points for the NFS file servers that make up the local area network. |
| `/Network/Users/` | Contains the home directories for all local-area network users. This is the default location for home directories. Home directories may also be stored on other servers.  |

The system domain contains the resources required by Mac OS X to run. All resources in the system domain are located in the `/System` directory on the root volume. These resources are provided by Apple and only the root user can modify the contents of this directory. Administrative users and applications cannot install resources in the system domain or modify its contents directly.

By default, the `/System` directory contains only a `Library` subdirectory. This subdirectory contains many of the same types of resources as other `Library` directories in the system. However, in the system domain, this directory also contains the core services, frameworks, and applications that make up Mac OS X. For more information on the `Library` directory, see [The Library Directory](The%20Library%20Directory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4delkciffeqq2ijjeq).

Mac OS X includes two public programmatic interfaces you can use to search for resources, plug-ins, and other items within specific directory locations of specific (or all) domains. One of these interfaces—the `FindFolder` function of the Folder Manager—is for Carbon or other C-based programs; for more information, see _Folder Manager Reference_. The other interface—the functions and constants defined in `NSPathUtilities.h` in the Foundation framework—is for [Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) programs; for more information, see _[Foundation Framework Reference](https://developer.apple.com/documentation/foundation)_.

Both interfaces help you search through all file-system domains for a particular item. By convention, searches typically begin with the most specific domain and end with the most general. This domain order is as follows:

1. User
2. Local
3. Network
4. System

Most system software follows this order when it searches for items through all file-system domains. However, you may search in any domain order that is appropriate to your application’s needs.

[Next](The%20Library%20Directory.md)[Previous](Introduction%20to%20the%20File%20System%20Overview.md)

