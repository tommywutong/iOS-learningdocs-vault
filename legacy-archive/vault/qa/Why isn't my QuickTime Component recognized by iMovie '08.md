---
title: Why isn't my QuickTime Component recognized by iMovie '08?
apple_id: DTS10004444
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2007-10-03'
source_url: https://developer.apple.com/library/archive/qa/qa1545/_index.html
archived_at: '2026-07-18T02:32:15.843489Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1545

# Why isn't my QuickTime Component recognized by iMovie '08?

## Q:  My QuickTime Movie Import Component supporting a custom file format works with iMovie HD but is being ignored by iMovie '08. What needs to be done to have iMovie '08 recognize it?

A: My QuickTime Movie Import Component supporting a custom file format works with iMovie HD but is being ignored by iMovie '08. What needs to be done to have iMovie '08 recognize it?

iMovie '08 requires that all components supporting your media (Importers('`eat` '), Exporters('`spit`'), Compressors('`imco`'), Decompressors('`imdc`') and so on) are thread-safe in order for the application to recognize and use them. If iMovie is asked to work with content requiring the use of a component that is not thread-safe, it will ignore that content.

For a discussion and some tips on how to make your QuickTime component thread-safe, see [Technical Note TN2125, 'Thread-safe programming in QuickTime'](https://developer.apple.com/technotes/tn/tn2125.html).

Once you've successfully made your component thread-safe make sure to set the `cmpThreadSafe` flag in your global component flags. This indicates to QuickTime (and applications such as iMovie) that your component can safely be used from background threads.

Additionally, if you've implemented an Export Component ('`spit`' component type), it must support the `MovieExportFromProceduresToDataRef` selector and have the `canMovieExportFromProcedures` component flag set.

These requirements are new with iMovie '08.

__Listing 1__  Component thread-safe and export from procedures flags.

```
cmpThreadSafe  = 1L << 28 // Component is thread-safe  canMovieExportFromProcedures  = 1 << 15 // Exporter implements MovieExportFromProceduresToDataRef
```


__Listing 2__  Adding the `cmpThreadSafe` flag.

```
// extended 'thng' template #define thng_RezTemplateVersion 1  #include <Carbon/Carbon.r> #include <QuickTime/QuickTime.r>  resource 'thng' (256) {     kSomeQTComponentType,     'DEMO',     'DEMO',     0,     0,     0,     0,     'STR ',     128,     'STR ',     129,     0,     0,     kMyComponentVersion,     // Registration Flags     componentHasMultiplePlatforms |  kOtherComponentRegistrationFlags,     0,     {       // Add Thread Safe Flag       kMyComponentFlags | cmpThreadSafe,     //*** ThreadSafe Flag Here        'dlle',        512,       platformPowerPCNativeEntryPoint     }; };
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-10-03 | New document that discusses why iMovie '08 may ignore 3rd party QuickTime Components. |

