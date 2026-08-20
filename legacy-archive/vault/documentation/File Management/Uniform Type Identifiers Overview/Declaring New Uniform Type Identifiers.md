---
title: Uniform Type Identifiers Overview
apple_id: TP40001319
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreServices
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_declare/understand_utis_declare.html
archived_at: '2026-07-15T07:32:27.941175Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Uniform Type Identifiers Overview](Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md)


[Next](Document%20Revision%20History.md)[Previous](Adopting%20Uniform%20Type%20Identifiers.md)

# Declaring New Uniform Type Identifiers

Mac apps can add new uniform type identifiers for proprietary data formats. You declare new UTIs in the information [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) (`info.plist`) file of a bundle. You can declare new UTIs in any of the following:

- Application bundles
- Spotlight Importer bundles
- Automator action bundles

In addition to declaring the UTI string, the declaration can contain any of the following properties:

- The type’s tag specification, specifying all the alternate identifier tags that match this type
- A list of UTIs to which this identifier conforms
- The icon to use when displaying items of this type
- A user-readable string describing this identifier, which the containing bundle may localize

Your UTI declarations must be either imported or exported:

- An exported UTI declaration means that the type is available for use by all other parties. For example, an application that uses a proprietary document format should declare it as an exported UTI.
- An imported UTI declaration is used to declare a type that the bundle does not own, but would like to see available on the system. For example, say a video-editing program creates files using a proprietary format whose UTI is declared in its application bundle. If you are writing an application or plugin that can read such files, you must make sure that the system knows about the proprietary UTI, even if the actual video-editing application is not available. To do so, your application should redeclare the UTI in its own bundle but mark it as an imported declaration.

If both imported and exported declarations for a UTI exist, the exported declaration takes precedence over imported one.

Here is a sample declaration for the `public.jpeg` UTI, defined as an exported type, as you would find in a property list:

```
 <key>UTExportedTypeDeclarations</key>
        <array>
            <dict>
                <key>UTTypeIdentifier</key>
                <string>public.jpeg</string>
                <key>UTTypeReferenceURL</key>
                <string>http://www.w3.org/Graphics/JPEG/</string>
                <key>UTTypeDescription</key>
                <string>JPEG image</string>
                <key>UTTypeIconFile</key>
                <string>public.jpeg.icns</string>
                <key>UTTypeConformsTo</key>
                <array>
                    <string>public.image</string>
                    <string>public.data</string>
                </array>
                <key>UTTypeTagSpecification</key>
                <dict>
                    <key>com.apple.ostype</key>
                    <string>JPEG</string>
                    <key>public.filename-extension</key>
                    <array>
                        <string>jpeg</string>
                        <string>jpg</string>
                    </array>
                    <key>public.mime-type</key>
                    <string>image/jpeg</string>
                </dict>
            </dict>
        </array>
```

[Table 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjzfvbuqmrqgqwvgvzt) shows a list of the available property key lists that you use in UTI declarations.

__Table 3-1__  Property list keys for uniform type identifiers

| Key | Value type | Description |
| `UTExportedTypeDeclarations` | array of dictionaries | An array of exported UTI declarations (that is, identifiers owned by the bundle’s publisher). |
| `UTImportedTypeDeclarations` | array of dictionaries | An array of imported UTI declarations (that is, identifiers owned by another company or organization). |
| `UTTypeIdentifier` | string | The UTI for the declared type. This key is required for UTI declarations. |
| `UTTypeTagSpecification` | dictionary | A dictionary defining one or more equivalent type identifiers. |
| `UTTypeConformsTo` | array of strings | The UTIs to which this identifier conforms. |
| `UTTypeIconFile` | string | The name of the bundle icon resource to associate with this UTI. |
| `UTTypeDescription` | string | A user-visible description of this type. You can localize this string by including it in an `InfoPlist.strings` file. |
| `UTTypeReferenceURL` | string | The URL of a reference document describing this type. |

If your application uses proprietary data formats, you should declare them in the `Info.plist` file of your application bundle. Follow these guidelines for best results:

- Your UTI string must be unique. Following the reverse-DNS format beginning with `com.`_companyName_ is a simple way to ensure uniqueness. While the system can support different UTI strings with the same specification, the reverse is not true.
- If your code relies on third-party UTI types that may not be present on the system, you should declare those UTIs as imported types in your bundle.
- Be sure to add conformance information if your proprietary type is a subtype of one or more existing types. In most cases you should not specify conformance to a nonpublic type, unless you are also declaring that type in your bundle. Although a custom UTI can conform to any UTI, `public.data` or `com.apple.package` must be at the root of the conformance hierarchy for all custom UTIs that are file formats (such as documents); otherwise, the system can’t tell if an item on disk has that UTI. For a list of public and Apple-defined UTIs, see [System-Declared Uniform Type Identifiers](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Articles/System-DeclaredUniformTypeIdentifiers.html#//apple_ref/doc/uid/TP40009259).

[Next](Document%20Revision%20History.md)[Previous](Adopting%20Uniform%20Type%20Identifiers.md)

