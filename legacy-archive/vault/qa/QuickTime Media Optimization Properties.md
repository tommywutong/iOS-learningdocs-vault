---
title: QuickTime Media Optimization Properties
apple_id: DTS10004589
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2009-03-30'
source_url: https://developer.apple.com/library/archive/qa/qa1579/_index.html
archived_at: '2026-07-18T02:32:19.856035Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1579

# QuickTime Media Optimization Properties

## Q:  What do the `AllowMediaOptimization` Movie Import and Movie Instantiation properties do?

A: Developers targeting QuickTime 7.3 and later may now opt-in for media optimization. Doing so will permit QuickTime to create Movies with optimal media representation without regard to the way the same source media may have been represented by QuickTime in the past.

There are two media optimization properties:

- `kQTMovieInstantiationPropertyID_AllowMediaOptimization` for use with `NewMovieFromProperties`.
- `kQTMovieImporterPropertyID_AllowMediaOptimization` for use when directly calling Movie Import Components.

As of QuickTime 7.3, media optimization is only supported by the MP3 Movie Import Component.

When the media optimization property is enabled, QuickTime is permitted to import MP3 files in a more accurate manner in which the sample offsets in the created media will correspond precisely to boundaries between MPEG audio packets in the packet stream.

QuickTime does not do this by default to maintain compatibility with some older applications that rely on the older MP3 importing behavior.

Using the media optimization property today will gain developer benefits in the future as support is added to QuickTime. The usefulness of this property becomes apparent by discussing a hypothetical MPEG file import operation.

When importing traditional .mpg files, QuickTime currently creates a Movie containing a single \*special\* MPEG Track type. However, if an application opts-in for media optimization, a future version of QuickTime is permitted to create the same Movie using a more optimal media representation if available; possibly a Movie with a separate Video Track and Sound Track in this case.

QTKit does not enable media optimization by default. Additionally, as of QuickTime 7.3 QTKit does not support a `QTMovie` instantiation attribute corresponding to `kQTMovieInstantiationPropertyID_AllowMediaOptimization` for use with `movieWithAttributes` or `initWithAttributes`.

QTKit developers who would like to use optimized import may call `NewMovieFromProperties` then create a `QTMovie` object using `movieWithQuickTimeMovie`.

Developers should __refrain__ from using media optimization for applications that manipulate QuickTime Movies in ways that rely on assumptions about a Movies internal structure. For example, the application assumes a Movie contains a specific number of Tracks or Track Types, assumes the version of the Sample Description structure or accesses fields of the Sample Description structures directly, assumes the size or type of media samples, assumes chunk sizes and so on.

These assumptions rely on specific QuickTime Movie creation behavior which may change when media optimization is enabled.

For example, older applications may still read sound media samples directly from the Sound Media Handler and therefore may implicitly rely on the assumption that QuickTime will always import audio media in a very specific way. If media optimization is enabled, this code may not behave as expected.

If an application allows QuickTime to interpret the contents of Movies and render them, it is certainly eligible and encouraged to enable media optimization.

__Listing 1__  Opting in for optimized Movie creation using `NewMovieFromProperties`.

```
OSStatus CreateMovieWithProperties(CFStringRef inPath, Movie *outMovie)
{
    // must have a valid path
    if (NULL == inPath) return paramErr;

    // create the property array
    QTNewMoviePropertyElement movieProps[4] = {0};

    // Store the movie properties in the array

    // Location
    movieProps[0].propClass = kQTPropertyClass_DataLocation;
    movieProps[0].propID = kQTDataLocationPropertyID_CFStringNativePath;
    movieProps[0].propValueSize = sizeof(inPath);
    movieProps[0].propValueAddress = (void*)&inPath;
    movieProps[0].propStatus = 0;

    Boolean boolTrue = true;

   // Ignore data references that cannot be resolved
    movieProps[1].propClass = kQTPropertyClass_MovieInstantiation;
    movieProps[1].propID = kQTMovieInstantiationPropertyID_DontAskUnresolvedDataRefs;
    movieProps[1].propValueSize = sizeof(boolTrue);
    movieProps[1].propValueAddress = &boolTrue;
    movieProps[1].propStatus = 0;

    // Allow QuickTime importers to optimize the media representation during import.
    // This may create media that is not fully compatible with applications that use older
    // low-level APIs to access and manipulate media samples.
    movieProps[2].propClass = kQTPropertyClass_MovieInstantiation;
    movieProps[2].propID = kQTMovieInstantiationPropertyID_AllowMediaOptimization;
    movieProps[2].propValueSize = sizeof(boolTrue);
    movieProps[2].propValueAddress = &boolTrue;
    movieProps[2].propStatus = 0;

    // Make the Movie active
    movieProps[3].propClass = kQTPropertyClass_NewMovieProperty;
    movieProps[3].propID = kQTNewMoviePropertyID_Active;
    movieProps[3].propValueSize = sizeof(boolTrue);
    movieProps[3].propValueAddress = &boolTrue;
    movieProps[3].propStatus = 0;

    return NewMovieFromProperties(4, movieProps, 0, NULL, outMovie);
}
```


__Listing 2__  Opting in for optimized import.

```
// Must be set when Component is first opened and prior to calling MovieImportDataRef etc.
OSStatus MyMovieImportAllowMediaOptimization(ComponentInstance inMovieImporter)
{
    Boolean allowMediaOptimization = true;

    // Hey importer, I want media optimization!
    return QTSetComponentProperty(inMovieImporter,
                                  kQTPropertyClass_MovieImporter,
                                  kQTMovieImporterPropertyID_AllowMediaOptimization,
                                  sizeof(Boolean),
                                  &allowMediaOptimization);
}
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-03-30 | Editorial |
| 2008-01-15 | New document that discusses the kQTMovieImporterPropertyID_AllowMediaOptimization and kQTMovieInstantiationPropertyID_AllowMediaOptimization properties. |

