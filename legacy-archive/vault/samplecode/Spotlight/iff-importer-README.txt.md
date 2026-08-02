---
title: Spotlight
apple_id: DTS10003713
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreServices
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/Spotlight/Listings/iff_importer_README_txt.html
archived_at: '2026-07-18T03:25:21.252560Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Spotlight](Spotlight.md)


[Next](NoteTaker-GetMetadataForFile.m.md)[Previous](iff-importer-main.c.md)

# iff-importer/README.txt

```
This code sample is a simple Spotlight plug-in (importer) that
publishes metadata for IFF image files.  It shows how to get a
rudimentary importer working and does not do anything except
publish the kMDItemPixelWidth and kMDItemPixelHeight attributes.

The one flaw of this importer is that it reads the entire file
into memory with the NSData method, dataWithContentsOfFile.  A
real image importer would only read the necessary pieces of the
header and/or only read in a fixed size chunk from the start of
the file.  Fortunately IFF images tend to be less than a few megs
in size so this isn't such a problem for this importer.
```

[Next](NoteTaker-GetMetadataForFile.m.md)[Previous](iff-importer-main.c.md)

