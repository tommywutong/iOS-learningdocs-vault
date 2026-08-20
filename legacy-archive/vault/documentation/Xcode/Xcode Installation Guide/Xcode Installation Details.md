---
title: Xcode Installation Guide
apple_id: TP40006599
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/XcodeCoexistence/Contents/Resources/en.lproj/Details/Details.html
archived_at: '2026-07-18T02:24:20.897785Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Installation Guide](Introduction%20to%20Xcode%20Installation%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Xcode%20Installation%20Basics.md)

# Xcode Installation Details

The main application in Xcode is `Xcode.app`, but the term Xcode is also used to refer to all the items installed by the Xcode Tools installer. After installing Xcode, the essential Xcode tools are contained in a single directory, known as the `<Xcode>` directory. By default, the Xcode Tools installer sets `/Developer` as the `<Xcode>` directory, but users can choose a different location for this directory. The user is free to rename the folder either during or after the install.

Even when a user chooses a custom location, unless the Developer Tools System Components choice is disabled, the installer will install the CHUD performance tools in `/Developer`. This is done to prevent multiple versions of CHUD from being installed on one system; only the last version of CHUD installed is functional. CHUD depends on components installed into the system by the Xcode Tools installer. You may move or rename the `/Developer` directory containing the CHUD tools, as long as the directory stays on the same machine and the same system partition is booted.

If the user has installed the developer system components, the `<Xcode>` directory may be located with the `xcode-select` tool. For more information, see [Xcode Command-Line Tools Installation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkojzfvbuqnrnknltcni).

The Xcode Tools installer adds content to the directories described in this section.

Table 2-1 lists the directories in which the installer places the content of each install group.

__Table 2-1__  Xcode Tools install destinations

| Install group | Destination |
| Developer Tools Essentials | `<Xcode>` |
| Developer Tools System Components | `/Developer, /usr, /Library, /System/Library/LaunchDaemons` |
| UNIX Development Support | `/usr` |
| Core Reference Library | `<Xcode>/Documentation/DocSets/com.apple.ADC_Reference_Library.CoreReference.docset` |
| Mac OS X 10.3.9 Support | `<Xcode>/usr/bin/gcc-3.3, <Xcode>/SDKs/MacOSX10.3.9.sdk` |

Table 2-2 lists the directories created by the Xcode Tools installer.

__Table 2-2__  Xcode Tools install directories

| Directory | Description |
| `<Xcode>` | The default is `/Developer`. |
| `/Library/Developer/<Xcode_release_number>` | Content in this location is specific to one Xcode release. |
| `/Library/Developer/Shared` | Content in this location is used by all releases of Xcode. |
| `/Developer` | When the Developer Tools System Components group is installed, the CHUD performance tools are installed in this location. |

Whether you’re a standard user or an administrator, you may want to customize an Xcode installation. For example, on a system with multiple Xcode installations, you may want to consolidate documentation in one place to reduce space usage. You may have developed a custom project template that needs to be accessible to several Xcode installations.

Note that for a particular Xcode release, Xcode applications look first in their `<Xcode>` directory, then the user’s home directory, and then the local domain. They do not look in, or have any knowledge of, other `<Xcode>` directories on the computer.

__User-Managed Directories__ allow users to customize their Xcode environments:

- `~/Library/Application Support/Developer/<Xcode_release_number>/`
- `~/Library/Application Support/Developer/Shared/`

For example, a user might want to install an Xcode project template in this directory:

- `~/Library/Application Support/Developer/Shared/Xcode/Project Templates/`

The primary type of content users need to install in these locations are templates. In general, templates should go in the Shared location. Content in the Shared location is used by all releases of Xcode, while content in an Xcode_release_number location is only used by that release. Users generally want their custom templates available no matter which version of Xcode is installed.

__Administrator-Managed Directories__ allow users with administrator privileges to customize Xcode environments:

- `/Library/Application Support/Developer/<Xcode_release_number>/`
- `/Library/Application Support/Developer/Shared/`
- `/Library/Developer/Shared`. The contents of this directory are used by all Xcode releases on the computer.

__The Shared Directory__ is a special case. If a system contains multiple Xcode releases, the `/Library/Developer/Shared` directory contains content for only one Xcode release—the last release installed. For example, if you install Xcode 3.0 and then Xcode 3.1 on the same computer, with the Developer Tools System Components group selected for both installs, `/Library/Developer/Shared` contains only Xcode 3.1 content.

The last release installed is the only release which is able to host distcc-distributed builds (see the "Share my computer for shared workgroup builds" option in Xcode's Distributed Builds preferences).

In Mac OS X v10.5 and later, developers can install and run Xcode 2.5 side-by-side with later versions of Xcode. Xcode 2.5 is the first version of the developer tools to support this feature. Apple recommends installing it alongside a later version if you need to support 2.x users or 2.x-only features (such as targeting Mac OS X 10.2.8).

When Xcode 2.5 is installed in Mac OS X v10.4, it resides in `/Developer` and behaves similarly to Xcode 2.4 and earlier releases. When Xcode 2.5 is installed in Mac OS X v10.5, you can choose the installation location. The default location is `/Xcode2.5`, so it does not remove or interfere with your Xcode 3 installation. In Mac OS X v10.5, Xcode 2.5 does not install the Developer Tools System Components, Unix Development Support, or WebObjects support. The Mac OS X v10.2.8 & v10.3.9 Support choice (off by default) installs some limited content in `/usr`.

Xcode 2.5 does not install performance tools in Mac OS X v10.5. Apple recommends using the Xcode 3 performance tools.

Xcode tools are not officially extensible. That is, there is no official support in Xcode for third-party tools such as compilers. The only exception is Intel and their C++ Compiler for Mac OS X. The installation of this compiler in Xcode is documented and supported by Intel.

For more information, see [Intel C++ Compiler Installation Guide](http://www.intel.com/software/products/compilers/docs/cmac/install.htm).

The `<Xcode>` directory, the main directory of the Xcode environment, contains the essential applications, command-line tools, and resources needed for developing software for Mac OS X. These are some of its subdirectories:

|  |  |
| --- | --- |
| `Applications` | Contains the applications and utilities used for software development. |
| `Documentation` | Contains API reference and high-level documentation. |
| `Examples` | Contains some example applications. You may incorporate sample code from these examples into your applications. |
| `Library` | Contains frameworks and resources used by Xcode applications. |
| `Platforms` | Contains the command-line tools and resources used for developing software for the platforms Xcode supports. Present in Xcode 3.1 and later. |
| `SDKs` | Contains the command-line tools and resources used for developing software using a specific SDK. |
| `usr` | Contains the Xcode UNIX command-line tools, libraries, man pages, and other resources. |

The Xcode Tools 3.0 installer also optionally installs the standard system development tools and interfaces into `/usr`, so conventional makeﬁle- and conﬁg-based builds will operate correctly.

In Xcode 3.0 and later, the Xcode directory has been re-structured to move developer tools content out of the underlying system and into a single top-level folder. Some of the more noticeable changes are listed here.

- The Xcode directory now has a `<Xcode>/usr` subdirectory that includes all command line developer content. For example, now `xcodebuild` is found at `<Xcode>/usr/bin/xcodebuild`, where previously it was located at `/usr/bin/xcodebuild`. Similarly, developer man pages, libraries, and other ﬁles can be found in the appropriate locations under `<Xcode>/usr`.
- In order to continue to support the UNIX model of developer tools being found in the boot volume and provide backward compatibility with external build systems, Xcode includes an optional install of this content into the boot volume. System headers and libraries are also provided for those projects that have not migrated to using SDKs.
- In an effort to better support multiple installations of the Xcode developer tools, the versions of `xcodebuild`, `xcodeindex`, `instruments`, `ibtool`, `opendiff`, and `agvtool` placed in `/usr/bin` are now shim scripts that work with the `xcode-select` tool (also located in `/usr/bin`) and reference the default version of the Xcode developer tools. Consult the `xcode-select(1)` man page for more information.
- Previously, supporting ﬁles for Xcode and other developer applications were located in `/Library/ Application Support/Apple/Developer Tools`. Now that content is located inside the Xcode directory in `<Xcode>/Library/`, with each application having its own folder. For example, support ﬁles for the Xcode application are located at `<Xcode>/Library/Xcode`. In addition, support ﬁles needed for a speciﬁc version of the tools can be placed outside the Xcode directory at `/Library/Application Support/ Developer/<tools version>` for support ﬁles needed for a speciﬁc version of the tools and `/Library/Application Support/Developer/Shared` for support ﬁles that are not speciﬁc to a given tools version. You are encouraged to place additional support ﬁles (like custom ﬁle or project templates) inside `<Xcode>/Library/` to allow the support ﬁles to move with the folder instead of being tied to the boot volume.
- Because a `<Xcode>/usr` folder hierarchy has been added to the Xcode directory, `<Xcode>/Tools` is being deprecated in Xcode 3.0 developer tools and will be removed in a future release of the tools. References to tools that used to exist in `<Xcode>/Tools` should be updated to ﬁnd their content in `<Xcode>/usr/bin`.
- Deprecated in a previous release, `ocvs` is no longer shipped as part of Xcode. Users of wrapped CVS repositories should transition to Subversion or CVS. In a related note, Subversion now ships as a part of Mac OS X v10.5 proper.
- The Java reference documentation for Java 1.4.2 and J2SE 5 is no longer part of the Xcode developer tools install and will be made available as a separate download on the ADC website. The Core Java Reference Library is still available via RSS subscription in the Xcode documentation window.
- The `ant`, `junit`, and `maven` command line tools are now part of Mac OS X v10.5 proper, so they are no longer shipped as part of Xcode developer tools.
- Jar Bundler and Applet Launcher have moved to `/usr/share/java` and are part of Mac OS X v10.5 proper, but are still accessible via symlinks in `<Xcode>/Applications/Utilities`.

Shimmed tools are command-line tools that are installed in `<Xcode>/usr/bin` but that have a counterpart in `/usr/bin`. This counterpart is not a complete program, but a shim or launcher that invokes one of its counterparts in an `<Xcode>` directory. These shims invoke the actual tools in the `<Xcode>` directory selected for CLI-based development, known as the Xcode CLI directory.

These are the Xcode _shimmed tools_:

- `agvtool`
- `ibtool`
- `xcodebuild`
- `xcodeindex`
- `instruments`
- `opendiff`

The shims determine which `<Xcode>` directory is the Xcode CLI directory through `xcode-select`. When writing software which needs to invoke Apple developer tools, your software should invoke `xcode-select -print-path` to find the path to your preferred developer tools install.

You specify the Xcode CLI directory on a shell session using the `DEVELOPER_DIR` environment variable or `xcode-select`.

When you install more than one Xcode release on your computer and need to use shimmed tools in scripts that are unaware of the location of the `<Xcode>` directory that contains the real tools, set the `DEVELOPER_DIR` environment variable to point to the desired `<Xcode>` directory or use the `xcode-select -switch` command.

For example, if you have Xcode 2.5 and Xcode 3.1 installed on your computer in `/Xcode_2.5` and `/Xcode_3.1`, respectively, and want to use the Xcode 2.5 shimmed tools in a script or in a shell session, do either of the following:

- Set the `DEVELOPER_DIR` environment variable:

```
export DEVELOPER_DIR="/Xcode_2.5"
```
- Use `xcode-select`:

```
sudo xcode-select -switch /Xcode_2.5
```

The Xcode Tools installer will set `xcode-select` to the `<Xcode>` directory it is installing unless the Developer Tools System Components choice is turned off.

See the man page `xcode-select` for more information.

When a user installs the UNIX Development Support group, the Xcode UNIX tools, libraries, and man pages are installed in `/usr` (in addition to `<Xcode>/usr`). This content can be used for traditional UNIX software development.

If you install more than one Xcode release and want to use the UNIX tools from one of those releases instead of the ones in `/usr`, change the `PATH` and `MANPATH` environment variables to list `<Xcode>/usr` first.

For example, if you want to use the UNIX tools in `<Xcode>/usr` instead of the ones in `/usr` when invoking those tools using relative paths (`gcc`, not `/usr/bin/gcc`), change the environment variables `PATH` and `MANPATH` (if you want to use the corresponding man pages) using one of two methods:

- You can use `xcode-select` to construct the paths:

```
export PATH=`xcode-select --print-path`/usr/bin:${PATH}
export MANPATH=`xcode-select --print-path`/usr/share/man:${MANPATH}
```
- Rely on the `DEVELOPER_DIR` environment variable. If you are writing a script for a Run Script phase in Xcode or building your UNIX project with an External Target in Xcode (external targets can be used to kick off makefiles or other external build systems), Xcode sets `DEVELOPER_DIR` to the path of the developer directory with which you're building.

  You can use `DEVELOPER_DIR` to construct the paths as follows:

```
export PATH=${DEVELOPER_DIR}/usr/bin:${PATH}
export MANPATH=${DEVELOPER_DIR}/usr/share/man:${MANPATH}
```

  If you're not going through Xcode at all, you can set `DEVELOPER_DIR` in your own environment and then rely on it when constructing paths.

When writing software that uses the Xcode UNIX tools, Apple recommends using the copy of those tools installed in `<Xcode>/usr` instead of `/usr`, because your users may not have tools in `/usr` if they have disabled the optional UNIX Development Support choice in the Xcode installer.
Your software can find the path to the `<Xcode>` directory with the `xcode-select` command (see previous section).

[Next](Document%20Revision%20History.md)[Previous](Xcode%20Installation%20Basics.md)

