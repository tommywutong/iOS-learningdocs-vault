---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Front-End.html
archived_at: '2026-07-15T07:31:01.923849Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Back End](Back-End.md#apple-ijqwg2znivxgi),
Previous: [Documentation](Documentation.md#apple-irxwg5lnmvxhiylunfxw4),
Up: [gcc Directory](gcc-Directory.md#apple-m5rwglkenfzgky3un5zhs)

---

#### 6.3.8 Anatomy of a Language Front End

A front end for a language in GCC has the following parts:

- A directory `language` under `gcc` containing source
  files for that front end. See [The Front End `language` Directory](Front-End-Directory.md#apple-izzg63tufvcw4zbniruxezldorxxe6i), for details.
- A mention of the language in the list of supported languages in
  `gcc/doc/install.texi`.
- A mention of the name under which the language's runtime library is
  recognized by `--enable-shared=package` in the
  documentation of that option in `gcc/doc/install.texi`.
- A mention of any special prerequisites for building the front end in
  the documentation of prerequisites in `gcc/doc/install.texi`.
- Details of contributors to that front end in
  `gcc/doc/contrib.texi`. If the details are in that front end's
  own manual then there should be a link to that manual's list in
  `contrib.texi`.
- Information about support for that language in
  `gcc/doc/frontends.texi`.
- Information about standards for that language, and the front end's
  support for them, in `gcc/doc/standards.texi`. This may be a
  link to such information in the front end's own manual.
- Details of source file suffixes for that language and `-x
  lang` options supported, in `gcc/doc/invoke.texi`.
- Entries in `default_compilers` in `gcc.c` for source file
  suffixes for that language.
- Preferably testsuites, which may be under `gcc/testsuite` or
  runtime library directories. FIXME: document somewhere how to write
  testsuite harnesses.
- Probably a runtime library for the language, outside the `gcc`
  directory. FIXME: document this further.
- Details of the directories of any runtime libraries in
  `gcc/doc/sourcebuild.texi`.

If the front end is added to the official GCC CVS repository, the
following are also necessary:

- At least one Bugzilla component for bugs in that front end and runtime
  libraries. This category needs to be mentioned in
  `gcc/gccbug.in`, as well as being added to the Bugzilla database.
- Normally, one or more maintainers of that front end listed in
  `MAINTAINERS`.
- Mentions on the GCC web site in `index.html` and
  `frontends.html`, with any relevant links on
  `readings.html`. (Front ends that are not an official part of
  GCC may also be listed on `frontends.html`, with relevant links.)
- A news item on `index.html`, and possibly an announcement on the
  [gcc-announce@gcc.gnu.org](mailto:gcc-announce@gcc.gnu.org) mailing list.
- The front end's manuals should be mentioned in
  `maintainer-scripts/update_web_docs` (see [Texinfo Manuals](Texinfo-Manuals.md#apple-krsxq2lomzxs2tlbnz2wc3dt))
  and the online manuals should be linked to from
  `onlinedocs/index.html`.
- Any old releases or CVS repositories of the front end, before its
  inclusion in GCC, should be made available on the GCC FTP site
  [ftp://gcc.gnu.org/pub/gcc/old-releases/](ftp://gcc.gnu.org/pub/gcc/old-releases/).
- The release and snapshot script `maintainer-scripts/gcc_release`
  should be updated to generate appropriate tarballs for this front end.
  The associated `maintainer-scripts/snapshot-README` and
  `maintainer-scripts/snapshot-index.html` files should be updated
  to list the tarballs and diffs for this front end.
- If this front end includes its own version files that include the
  current date, `maintainer-scripts/update_version` should be
  updated accordingly.
- `CVSROOT/modules` in the GCC CVS repository should be updated.

- [Front End Directory](Front-End-Directory.md#apple-izzg63tufvcw4zbniruxezldorxxe6i): The front end `language` directory.
- [Front End Config](Front-End-Config.md#apple-izzg63tufvcw4zbninxw4ztjm4): The front end `config-lang.in` file.
