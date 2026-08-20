---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/BSDInfluences.html
archived_at: '2026-07-15T08:15:23.406957Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](Access%20Control%20Lists.md)[Previous](Display%20Names.md)

# BSD Permissions and Ownership

At a fundamental level, Mac OS X is a BSD system. A part of this underpinning is the way BSD implements ownership of, and permissions for, files and folders in the file system. This model, in turn, controls which users can read, write, rename, and execute files, and which users can copy and move files to and from folders. Although the file ownership model is conventionally associated with UFS or similar file systems, Mac OS X extends it to all supported file systems, including Mac OS Standard (HFS) and Mac OS Extended (HFS+).

The following sections describe the basic file ownership model, pointing out areas where Mac OS X differs. These sections also contain a discussion of how root and admin user accounts affect file management.

For each folder and file in the file system, BSD has three categories of users: owner, group, and other. For each of these types of user, three specific permissions affect access to the file or folder: read, write, and execute. If a user does not have read permissions in any of the categories for a file, the user cannot read the file. Similarly, if a user does not have execute permissions for an application, the user cannot run the application.

- The _owner_ of a folder or file is generally the user who created it. Owners typically have full privileges (read, write, and execute) for that file or folder. The owner of a file can set the permissions for other classes of users. The root user is the only user that can transfer ownership of files.
- Every user on the system also belongs to one or more groups. A _group_ is a named collection of users that have something in common. Every file has a group owner associated with it. The group owner can give additional permissions to a particular set of users. For example, if you had a group containing the engineers for a specific project, you would likely give that entire group write permissions for the source files in the project’s code repository.

  The system administrator is responsible for setting up groups.
- Users in the _other_ category are just that—everyone who is neither the owner of a file or a member of the group associated with a file. Permissions for this type of user are generally the most restrictive.

In a Terminal window, if you enter the command `ls -l` for some location in the file system (say, `~steve/Documents`), you get results similar to these:

```
total 3704
drwxrwxrwx  5 steve  staff  264 Oct 24 20:56 General
drwxrwxr-x  5 steve  admin  264 Oct 21 21:47 ProjectDocs
drwxr-xr-x  6 steve  staff  160 Oct 25 12:00 Planning
drwx--x--x  6 steve  staff  160 Oct 21 15:22 Private
-rwxrwxrwx  1 steve  staff    0 Oct 23 09:55 picture clipping
[sponge:~/Documents] steve%
```

The results show, among other things, the owner and primary group for a file or folder and the permissions for each type of user. The owner of a file is shown in the third column and the primary group is shown in the fourth. Thus, in the preceding listing, the `General` folder is owned by user `steve` and the group is `staff`.

The first column in a detailed file listing is a set of ten characters. The first character indicates the type of the item. A hyphen indicates an ordinary file, a `d` indicates a folder (directory), and an `l` indicates a symbolic link. The remaining nine characters fall into three implicit groups representing the permissions for the owner, group, other user types. The `r`, `w`, and `x` characters, if present, indicate that read, write, and execute permissions are turned on for the type of user the set of bits applies to.

To give an example of how to read the permissions of a file, the following listing shows the permissions for the `Planning` folder in `~steve/Documents`:

```
drwxr-xr-x  6 steve  staff  160 Oct 25 12:00 Planning
```

In this example, the item is a folder. The owner permissions are `rwx`, so the owner view the contents of the directory, can copy files and folders to this directory, can make it his or her current working directory (through the `cd` command), and can execute any program in it. The permissions for both the `staff` group and other users are both `r-x`, meaning that those users can read files in the directory and make it their current working directory; however, they cannot write files to the directory or modify or delete files in it.

If you have the appropriate permissions, you can change owner, group, and individual permissions from a Terminal shell using, respectively, the `chown`, `chgrp`, and `chmod` commands. (See the associated man pages for details.) You can also see the same ownership and permissions information for a selected file or folder in the Privileges pane in an Info window in the Finder. If you are the owner of the file or folder, you can also change permissions directly from the Info window.

To change the individual permissions for a file, you must be able to specify the desired permissions as three-digit integer. In this scenario, each read, write, execute triplet is represented as a decimal number between 0 and 7. Table 1 lists the relationships between each number and triplet.

__Table 1__  File permission mappings

| Decimal number | Permission | English translation |
| 0 | --- | No permissions |
| 1 | --x | Execute only |
| 2 | -w- | Write only |
| 3 | -wx | Write and execute |
| 4 | r-- | Read only |
| 5 | r-x | Read and execute |
| 6 | rw- | Read and write |
| 7 | rwx | Read, write, and execute |

For example, suppose you have a directory whose contents are visible only to the owner. In this case, the directory listing might look something like this:

```
drwx--x--x  6 steve  staff  160 Oct 21 15:22 Private
```

To get the permissions specified here, the owner would have had to execute a command similar to this one:

```
chmod 711 ./Private
```

To break this command down, the `chmod` command changes the individual permissions for the specified item. The number `711` represents the overall permissions for the directory. The first digit (`7`) represents the triplet `rwx`. The second and third digits (both `1`) represent the triplet `--x`.

When you build an application with Xcode, the build subsystem automatically sets the permissions of the executable file to `-rwxr-xr-x`; this setting enables the owner—that is, the person who installs the application—to execute and write to the application, whereas all others can only execute it. Other IDEs set similar permissions on built executables.

The `-rwxr-xr-x` setting should suffice except in the rare situations where an application requires privileged (root) access. An example would be an application such as a disk repairer that required low-level hardware access through the kernel. In such cases, you could use the `setuid` command to acquire root access for the application. You could then use the features of the NetInfo Kit and System [frameworks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) that allow you to authenticate administrators. For more information on `setuid`, consult the `setuid (2)` and `chmod (1)` man pages.

Although the permission set of the application determines who can launch an application, once it is launched, the application process is owned by the user who launched it. This means the application has the same access rights as the logged-in user and inherits the permissions of that user account. These permissions affect many aspects of the application, such as where the application can save user documents. The application can save files only to locations for which the user has appropriate permissions.

When a Carbon, [Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9), or Java application saves a document, the respective application environment automatically sets the permissions of the document to (`-rw-r--r--`) by default, giving the owner read and write access but limiting other users to only read-only access. If you want different permissions for the documents created by your application, you must set those permissions using an appropriate file-management interface. For Carbon, use the interfaces of the File Manager. For Cocoa, use the NSFileManager class. 

In Mac OS X, administrative and root accounts give you extended access to modifying the file system.

On BSD systems there is a root user account, which has unlimited access to the folders and files on the system. The root user is often known as the superuser because of the superior access available to that account. For example, a root user can perform the following tasks:

- Read, write, and execute any file
- Copy, move, and rename any file or folder
- Transfer ownership and reset permissions for any user

On BSD systems, root-level access is also available to members of the `wheel` group. Membership in this group confers on users the ability to become the superuser temporarily. To gain this ability, the user enters `su` at the command line and then enters his or her password when prompted for it. Superuser access grants the user temporary root access without requiring the user to logout and log back in as `root`.

In Mac OS X, the root user account is disabled by default to improve system security. The disabling of the root account prevents users from gaining superuser privileges, including through use of the `su` command.

Although the root account is disabled, Mac OS X establishes an admin user account when the system is first installed. The admin user can perform most of the operations normally associated with the root user. The only thing the admin user is prevented from doing is directly adding, modifying, or deleting files in the system domain. However, an administrator can use the Installer or Software Update applications for this purpose.

Any user on the system may have administrative privileges, that is, there is no special need for an account with the name `admin`. Admin users gain their privileges by being added to the `admin` group; non-administrative users belong to the `staff` group. An admin user can grant administrative rights to other users of the system using the Accounts pane of System Preferences.

Although the root user is disabled by default, an administrative user can reenable it and acquire superuser status. To reenable the root user, do the following:

1. Launch the NetInfo Manager application in `/Applications/Utilities`.
2. Choose Security > Authenticate (as needed) to authenticate yourself as an administrative user. (A domain window must be open in order to authenticate yourself.)
3. Choose Security > Enable Root User. (This menu item is enabled only if you are an authenticated member of the local `admin` group.)

The root user password is blank by default. When you enable the account, you are prompted for a root password automatically. You should always provide a root password for security reasons.

After you’ve completed the task requiring root access, you should relinquish superuser privileges immediately by choosing Security > Disable Root User in the NetInfo Manager application.

[Next](Access%20Control%20Lists.md)[Previous](Display%20Names.md)

