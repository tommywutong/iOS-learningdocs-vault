---
title: MoreIsBetter
apple_id: DTS10000732
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MoreIsBetter/Listings/MIB_Libraries_MoreCodeFragments_CFMLateImport_CallMachOFramework_System_Framework_Stub_Stub_Library_Read_Me_txt.html
archived_at: '2026-07-18T03:15:22.314636Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoreIsBetter](MoreIsBetter.md)


[Next](MIB-Libraries-MoreCodeFragments-CFMLateImport-CFMLateImport.c.md)[Previous](MIB-Libraries-MoreCodeFragments-CFMLateImport-CallMachOFramework-Read%20Me%20CallMac.md)

# MIB-Libraries/MoreCodeFragments/CFMLateImport/CallMachOFramework/System Framework Stub/Stub Library Read Me.txt

```
Stub Library Read Me

This folder contains a dummy stub library that you use to satisfy the linker 
when using the CFMLateImport approach for calling Mach-O frameworks from CFM. 
The current stub library, SystemFrameworkLib, exports just a single symbol 
(gethostname). You can expand this list by editing the export file 
(SystemFrameworkStub.exp) and rebuilding the stub library using the 
MPW MakeStub command.

    MakeStub SystemFrameworkStub.exp -fragname SystemFrameworkLib -o SystemFrameworkLib.stub

You can download MPW from the Apple developer web site.

    <http://developer.apple.com/tools/mpw-tools/>

You can also build stub libraries with CodeWarrior Pro 6, but those libraries 
have certain quality problems that I find disturbing. I have reported those 
problems to Metrowerks.  Until they are fixed I will stick with MPW, however 
your mileage might vary.

To build a stub library for all of the symbols in a framework, you need a list 
of those symbols. You can generate this list using the Mac OS X nm command line 
tool.  Type man nm on the command line for details.

Share and Enjoy.

Worldwide Developer Technical Support

8 Oct 2001

$Log: Stub\040Library\040Read\040Me.txt,v $
Revision 1.1  2001/10/08 14:20:32         
Add .stub extension.
```

[Next](MIB-Libraries-MoreCodeFragments-CFMLateImport-CFMLateImport.c.md)[Previous](MIB-Libraries-MoreCodeFragments-CFMLateImport-CallMachOFramework-Read%20Me%20CallMac.md)

