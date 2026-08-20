---
title: Documentation Set Guide
apple_id: TP40005266
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2009-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Documentation_Sets/090-docsetutil_Reference/docsetutil.html
archived_at: '2026-07-15T07:24:25.719214Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Documentation Set Guide](Introduction.md)


[Next](Documentation-Set%20Property%20List%20Key%20Reference.md)[Previous](Testing%20and%20Packaging%20Documentation%20Sets.md)

# docsetutil Reference

Apple provides the command-line tool `docsetutil` to help you create, test, and query full-text and API indexes for your documentation set. To use the tool, open Terminal and enter the following:

```
docsetutil <verb> [options] <doc_set_path>
```

The `<doc_set_path>` argument specifies the file system path to the documentation set bundle and is required for all operations using `docsetutil`.

You can use `docsetutil` to:

- Generate full-text and API indexes
- Search for a particular string in the indexes
- Validate the indexes
- Print index content
- Generate a downloadable update

The `docsetutil` tool supports the following common options, which you can use with any of the available verbs:

- `-localization <locale>`. The locale to use when operating on the documentation set. Use this option to index or search localized documentation set content. The `<locale>` argument should be one of the standard locale designations, as described in “Language and Locale Designations.”

  When you specify a locale for indexing, the `docsetutil` tool uses the most appropriate metadata files for the specified locale to create the index files. It stores the generated index files in a `<locale>.lproj` subdirectory of the `Resources` directory. Without this option, `docsetutil` creates global indexes, stored at the top level of the `Resources` directory, although it uses the most appropriate metadata files for the current user’s preferred language.
- `-verbose`. Print additional information about the operation.
- `-debug`. Print additional debugging information about the tool and any errors.

These are the available verbs and their corresponding options:

- `help`. Print a list of the `docsetutil` tool’s command-line options.
- `index`. Generate indexes for the specified documentation set. These are this verb’s options:

  - `-fallback <path>`. The path to a local copy of the web content associated with the documentation set. This is the web content at the location specified by the documentation set’s [DocSetFallbackURL](Documentation-Set%20Property%20List%20Key%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqnbnknltg) property. If the documentation set splits its content between the locally installed documentation set bundle and additional files on the web, you must create a local copy of the web content for indexing. When a documentation node—as listed in the `Nodes.xml` file—is not found in the documentation set bundle, the `docsetutil` tool looks at the location specified by the fallback argument and uses the files it finds there for the full-text index.
  - `-node <node_path>`. (Documentation-set debugging) The path to the documentation node that you want to index. This option indexes the specified node and any subnodes it might have. `<node_path>` is a colon-separated string of node names, such as `Core Reference:Cocoa`. The root node is optional. Node names must match exactly the `Name` element in the nodes file.
  - `-download`. Downloads and indexes the landing page associated with any node that specifies an Internet address as its location using the URL element. The `docsetutil` tool downloads only the node’s landing page. It does not download the folder or folder hierarchy of content associated with a folder or bundle node.
  - `-skip-text`, `-skip-api`. Prevents the creation of either the full-text or API indexes, respectively. By default, the indexer creates both the full-text and API indexes. You can use these flags to disable one of these indexes.
- `search`. Query the existing indexes for the given string and report any matches. This allows you to test indexes that you have previously generated. These are this verb’s options:

  - `-query <string>`. The string to search for in the specified indexes. This option is required.
  - `-node <node_path>`. The path to the documentation node that you want to search. This is useful for limiting the scope of your search to a particular node in the documentation set, and any subnodes that it might have. `<node_path>` is a colon-separated string of node names, such as `Core Reference:Cocoa`. The root node is optional.
  - `-skip-text`, `-skip-api`. Skip either the full-text or API indexes, respectively. By default, `docsetutil` searches both the full-text and API indexes. You can use these flags to remove either of these indexes from the search, which is useful for limiting the scope of your search during testing.
- `dump`. Print the contents of existing indexes. This is useful for testing the indexes and ensuring that all expected information is present. This command also prints useful statistics about these indexes, such as the total number of nodes and tokens in them. This verb’s options are:

  - `-node <node_path>`. The path to the documentation node whose contents you want to print. Use this option to limit the scope of the printed information. The `docsetutil` tool prints the contents of the specified node, including its subnodes. `<node_path>` is a colon-separated string of node names, such as `Core Reference:Cocoa`. The root node is optional.
  - `-toc-depth <toc_levels>`. The number of levels of the documentation hierarchy that you want to print. You can use this option to restrict the printout of the documentation set’s table of contents to a particular depth.
  - `-text-depth <text_levels>`. The number of levels of information you want `docsetutil` to print from the full-text index. Possible values are:

    - `0`: `docsetutil` prints only the names of the root locations. The root locations include the location of the local documentation set bundle (the default root), any location specified by the `DocSetFallbackURL` property, and any other base URL locations specified by individual nodes in the `Nodes.xml` file.
    - `1`: (Default) `docsetutil` prints the root locations and the relative path to each of the nodes found at those root locations.
    - `2`: `docsetutil` prints the root locations, the path to each of the nodes therein, and the path to each HTML file indexed for each node.
  - `-skip-text`, `-skip-api`. Skip either the full-text or API indexes, respectively. By default, `docsetutil` prints the contents of both the full-text and API indexes. You can use these flags to disable one or both of these indexes. This is useful for limiting the size of the printout during testing. If you use both of these flags together, `docsetutil` prints only the document hierarchy.
- `validate`. Compare the contents of the indexes to the contents of the documentation set bundle and report any discrepancies.
- `package`. Package the documentation set bundle as an XAR archive. Options:

  - `-output <package_path>`. The pathname of the archive to create. If no output path is specified, docsetutil places the XAR archive in the same directory as the documentation set bundle. The archive’s name, in this case, is the same as the documentation set bundle name, but with the extension `xar` instead of `docset`.
  - `-signid <identity_name>`. The identity to use when adding a digital signature to the XAR archive. `docsetutil` looks through the user’s keychains for an identity with this name.
  - `-atom <atom_path>`. The path of the Atom feed to update with a new entry (or update an existing entry with the same version number) populated with all the available metadata about the documentation set and, if used, its signing identity. If the file does not exist, an Atom feed file is created.
  - `-download-url <URL>`. The URL at which the package is placed. This URL is used to create the feed entry. If not specified, a placeholder is put into the feed entry and you need to edit the entry before publishing it.

[Next](Documentation-Set%20Property%20List%20Key%20Reference.md)[Previous](Testing%20and%20Packaging%20Documentation%20Sets.md)

