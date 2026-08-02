---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/SCMManagingProjects/SCMManagingProjects.html
archived_at: '2026-07-15T07:28:48.632017Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Managing%20Files.md)[Previous](Overview%20of%20Version%20Control.md)

# Managing Projects

Xcode provides an easy-to-use interface to
your version control client tool; you can perform the most common
version control tasks as you perform normal development tasks. However,
there are some tasks you must perform using your client tool, such
as adding projects to a repository and checking out projects. You
seldom need to perform these tasks. For example, you need to check
out a project to work on it for the first time on a particular computer.
See [Using CVS](Using%20CVS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgywueq2jjjcuir2k) and [Using Subversion](Using%20Subversion.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrxgewueqsdjjceirsg) for details.

This chapter describes the files that store project and user
information for Xcode projects. You manage these files like any
files that you modify directly during development under version
control. This chapter also shows how to configure access to the
repository a project is housed in.

Xcode saves project metadata and individual developer settings
in the _project package_, which is named after
the project and with the extension `.xcode`.
(Earlier versions of Xcode used the `.pbproj` or `.pbxproj` extensions.)
The project package is located in the project directory, for example, `Sketch/Sketch.xcode`.
This package contains two files that you need to pay particular
attention to in order to keep the project package in sync with the
rest of the files in the project and to maintain personal project
settings in the repository: The project file and the user file.

- The project
  file, which Xcode maintains in the project package under the name `project.pbxproj`,
  stores project-related information, such as the files that are part
  of the project, the groups in the Groups & Files list, build
  settings, target definitions, and so on. Xcode constantly writes
  out this file; therefore, most of the time its status is 'M' (for details
  on file status codes, see [Viewing File Status](Managing%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrxgawugsscivdeursf)).

  If
  you make structural changes to the project, such as adding or removing
  files, you must commit this file along with the other changes (for
  example, when you commit a file you added to your working copy,
  you must also commit the project package). Otherwise, the project
  file may become out of sync with the rest of the project’s files (source
  code files, resource files, and so on).
- The user file stores user-related information, such as bookmarks,
  the active build style, and so forth. Xcode maintains this file
  inside the project package as `<username>.pbxuser`.
  So, for the user name `clare`,
  the corresponding user file is called `clare.pbxuser`.

  Xcode
  adds your user file to a project package when you open the project
  if there isn’t a user file for you inside the package. You should
  include your user file in your commits and updates if you want to
  safeguard your personal settings for the project in the repository
  or if you work on the project on more than one computer and want
  to use the same settings on all of them.

A _managed project_ is one whose root directory
is stored in a repository and whose access is controlled by a version
control system. Before you can work on a managed project, you must
check it out of the repository into a local copy.

After you check out a project directory, you must open the
project in Xcode and configure your repository-access settings.
These include the name of the version control system that manages
the repository, the path to the client tool, authentication information,
and whether version control is active. These settings are saved
in your user file in the project package. For more information on
the project package, see [Project Packages](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwhewueqkkizbucskj).

Follow these steps to configure your repository-access settings
for a project:

1. Open the
   project in Xcode.

   If you use a version control system that
   locks files in working copies, you may have to tell it that you
   intend to modify the project package before opening the project.
   For example, with Perforce, you would execute the following commands:

```shell
% cd ~/Working/Echo
% p4 edit Echo.xcode/...
% open -a Xcode Echo.xcode     # Or open it using the Xcode Open  command.
```
2. Choose your version control system from the SCM System pop-up
   menu in the General pane in the Project Info window, shown in Figure 21-1.

   __Figure 21-1__  The SCM System pop-up menu

   !
3. Tell Xcode how to use your client tool.

   Click Edit and
   enter the path to the client program in the client configuration
   dialog.

   If you use SSH to access a CVS repository, select
   “Use ssh instead of rsh for external connections” as shown in Figure 21-2.
   See [Accessing a CVS Repository](Using%20CVS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgywueq2jinceor2g) for further
   details.

   __Figure 21-2__  Client configuration dialog for CVS

   !
4. Activate version control for your copy of the project.

   Select
   Enable SCM in the General pane in the Project Info window.

   If
   you use SSH to access a Subversion repository, Xcode may ask you
   to enter your passphrase in the Authentication dialog, shown in Figure 21-3.

   __Figure 21-3__  Authentication dialog for Subversion

   !

   If Xcode is
   unable to talk to your client, a dialog describing the problem appears.
   In it you may choose to disable SCM or to leave it enabled. For
   example, if you try to access a project that contains wrapped bundles
   with a version of CVS that doesn’t support wrappers, the dialog
   shown in Figure 21-4 appears.

   __Figure 21-4__  SCM
   Error dialog

   !
5. Commit your user file to the repository.

   This step is
   not required; however, saving your user file in the repository provides
   two main benefits:

   - It ensures that you’ve
     correctly configured version control for your working copy of the
     project.
   - It allows you to use the same personal settings for the project
     in any computer you use to work on it.

You now know how to set up version control in your projects. [Managing Files](Managing%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrxgawueqkkivbeeq2i) explains
how to add version control operations to your development workflow.

[Next](Managing%20Files.md)[Previous](Overview%20of%20Version%20Control.md)

