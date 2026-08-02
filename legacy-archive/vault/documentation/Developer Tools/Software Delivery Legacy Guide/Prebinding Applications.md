---
title: Software Delivery Legacy Guide
apple_id: TP40004615
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2010-09-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SoftwareDistribution4/Prebinding/Prebinding.html
archived_at: '2026-07-15T07:26:58.727381Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Software Delivery Legacy Guide](Introduction.md)


[Next](Preserving%20Resource%20Fork%20Data.md)[Previous](Specifying%20System%20and%20Volume%20Requirements%20in%20Pre-Tiger%20Systems.md)

# Prebinding Applications

In Mac OS X v10.3.3 and earlier, when a Mach-O–based executable is launched, the dynamic link editor (or dynamic linker) loads the symbols that the executable imports at predetermined addresses in the executable’s address space. Prebinding is the process of computing the addresses for the imported symbols, so that the dynamic linker needs to perform less work at launch time. In other words, the launch time of an executable is optimized when these precomputed addresses contain valid data. With outdated prebinding information, an executable takes longer to load. The dynamic linker Mac OS X v10.3.4 and later is implemented in a way that makes prebinding unnecessary. But applications that need to run in earlier versions of Mac OS X may benefit from having their prebinding information up to date.

When you build an application targeted at Mac OS X versions earlier than v10.3.4, the addresses of its imported symbols are computed using the SDK you choose for the project. For example, an application built using the 10.2.8 SDK that is installed on a computer running Mac OS X v10.2.3 would need to have its prebinding information recomputed in order to optimize its launch time. In managed installs, the Installer application automatically performs this update. In manual installs, however, you must perform this task.

The `update_prebinding(1)` command-line tool updates an executable’s prebinding information. To optimize the launch time of a manually installed application, users need to run this tool after installing an application. You can provide instructions for how to run this tool in a Read Me file, printed documentation, or other mechanism.

For more information on prebinding, see _[Launch Time Performance Guidelines](../../Performance/Launch%20Time%20Performance%20Guidelines/Introduction%20to%20Launch%20Time%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2dq2i)_.

[Next](Preserving%20Resource%20Fork%20Data.md)[Previous](Specifying%20System%20and%20Volume%20Requirements%20in%20Pre-Tiger%20Systems.md)

