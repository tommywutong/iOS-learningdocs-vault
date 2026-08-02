---
title: Spotlight Importer Programming Guide
apple_id: TP40001267
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/Concepts/AssigningDataToAttrs.html
archived_at: '2026-07-15T05:23:19.182970Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Spotlight Importer Programming Guide](About%20Spotlight%20Importers.md)


[Next](Spotlight%20Importer%20Schema%20Format.md)[Previous](Extracting%20Metadata%20from%20Files.md)

# Assigning Values to Metadata Attributes

Spotlight defines standard metadata attributes that provide a wide range of options for storing your application’s file metadata. For users to be able to find data easily, it is important that you use standard metadata attributes whenever possible.

Spotlight provides standard metadata attributes for the following:

- File system attributes. For example, file size, owner, and modification date. These are extracted from the file system automatically by Spotlight.
- Image-related attributes. For example, bits per sample, color space, pixel height, and width.
- Video-related attributes. For example, codec, video bit rate, and audio bit rate.
- Audio-related attributes. For example, sample rate, track number, composer, and time signature.
- Attributes common to many applications. For example, authors, city, organization, email addresses, and headline.

The standard metadata attributes are documented in _[File Metadata Attributes Reference](../../File%20Metadata%20Attributes%20Reference/About%20the%20File%20Metadata%20Attributes%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmobz)_.

In addition to the context-specific attributes, Spotlight provides a general text attribute (`kMDItemTextContent`) that importers can populate with a text representation of a file’s content. Applications can create queries that reference this attribute, but are not able to read the value of this attribute directly.

You should avoid creating your own metadata attributes if an existing attribute key would be appropriate. For example, if your file’s metadata includes the photographer of an image, use the `kMDItemAuthors` attribute rather than defining a custom photographer attribute. Or, if your file includes a company name, use the `kMDItemOrganizations` attribute.

See [Assigning Values to Metadata Attributes](Writing%20a%20Spotlight%20Importer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenzvfuzdaobrgq3q) for an example of how to assign values to metadata attributes.

A Spotlight importer can provide localized values for an attribute by returning a dictionary object instead of a string value. The dictionary must contain keys that correspond to the localized languages. For example “en” for English, “fr” for French, and so forth. The value for each key should be the corresponding localized attribute value.

If none of the standard Spotlight attributes are appropriate or adaptable to your metadata, you can define a custom metadata attribute. An importer specifies the name of the custom attribute, as well as the type of data it contains, in its `schema.xml` file.

Custom metadata attributes must have unique names. To ensure a name is unique use the reverse DNS naming convention as a prefix for keys that are specific to your file types, replacing “.” with “_” characters. For example, the Mail program would prefix its custom attributes with `com_apple_mail`.

You must specify the type of object that is returned in your custom attribute. The supported types are `CFString`, `CFNumber`, `CFBoolean`, and `CFDate`.

If your custom attributes can contain multiple objects, declare them as multi-value in your importer's schema file and always return an array, even if it contains only a single instance.

Spotlight importers that declare custom metadata attributes should also provide a display name and description for each attribute. These strings are contained in the file `schema.strings` in the Spotlight importer bundle.

The file must be UTF-16 text, encoded formatted as a standard strings file. The display name keys correspond to the custom metadata attribute’s name. The description string is specified by appending “`.Description`” to the key name. Listing 1 shows a sample schema.strings file.

__Listing 1__  Sample importer’s schema.strings file

```
"com_apple_myCocoaDocumentApp_myCustomDocument_notes" = "Notes";
"com_apple_myCocoaDocumentApp_myCustomDocument_notes.Description" = "What it is you're supposed to remember.";
```

You can localize `schema.strings` files using the standard conventions.

[Next](Spotlight%20Importer%20Schema%20Format.md)[Previous](Extracting%20Metadata%20from%20Files.md)

