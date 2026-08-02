---
title: MoreIsBetter
apple_id: DTS10000732
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MoreIsBetter/Listings/MIB_Documentation_MoreDocumentation_BuildingAndUsing_html.html
archived_at: '2026-07-18T03:15:16.526351Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoreIsBetter](MoreIsBetter.md)


[Next](MIB-Documentation-MoreDocumentation-ContributingToMoreIsBetter.html.md)[Previous](MIB-Documentation-MoreDocumentation-banner.html.md)

# MIB-Documentation/MoreDocumentation/BuildingAndUsing.html

```swift
<HTML>
<HEAD>
   <TITLE>Building and Using MoreIsBetter</TITLE>
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<H1><!--Copyright (c) Apple Computer, Inc., 1998-2001-->Building
MoreIsBetter</H1>

<BLOCKQUOTE><H2>Tools</H2>

   <BLOCKQUOTE><H3>CodeWarrior Pro 8.3</H3>

      <P>This release of MoreIsBetter builds with CodeWarrior Pro 8.3.</P>

      <H3>Project Builder 2.1 (Dec 2002 Developer Tools)</H3>
                <P>MoreIsBetter also builds with on Mac OS X 10.2 with Project Builder 2.1 (Dec 2002 developer tools). Your mileage might vary on older or newer versions of Project Builder.</P>
                <p></p>
            </BLOCKQUOTE>

   <H2>Building</H2>

   <P>As long as you preserve the relative position of the folders as
   originally distributed with the MIB package, you should have no
   trouble building any part of MIB with a properly integrated tool
   set as described above. The access paths should all be set up
   relative to the projects. If you run into trouble with missing
   files, the most common access path you'll need to set up is
   <CODE>":MIB-Libraries:</CODE>"; this is where all the library code
   lives, and the various clients (demos, etc.) don't use each
   others' code, so you should be able to concentrate on getting one
   client at a time to build.</P>

   <P>Unless otherwise noted, all MoreIsBetter modules build for
   PowerPC, Carbon (CFM), and Carbon (Mach-O). Support for 68K is
   still included in many projects, but as none of the supported
   development tools support 68K we can no longer test this
   support.</P></BLOCKQUOTE>
</BODY>
</HTML>
```

[Next](MIB-Documentation-MoreDocumentation-ContributingToMoreIsBetter.html.md)[Previous](MIB-Documentation-MoreDocumentation-banner.html.md)

