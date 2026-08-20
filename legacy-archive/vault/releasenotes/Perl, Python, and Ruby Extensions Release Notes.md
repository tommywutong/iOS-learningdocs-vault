---
title: Perl, Python, and Ruby Extensions Release Notes
apple_id: TP40006659
resource_type: Release Note
platform: macOS
topic: Languages & Utilities
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/OpenSource/PerlExtensionsRelNotes/index.html
archived_at: '2026-07-18T02:59:02.061918Z'
---
> 导航：[总目录](../README.md) · [releasenotes](../_indexes/releasenotes.md)



# Creating Universal Extensions for Perl, Python and Ruby

With the advent of the Intel processor to the Macintosh family, software needs to be compiled/linked to run on multiple architectures. In OS X v10.4 and previous, extensions built by `perl`, `python` and `ruby` would only normally build for the native architecture. In OS X v10.5 and later, extension are built universal by default, and this can be customized.

#### Contents:

- [Building Universal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnjzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Building Perl, Python and Ruby Extensions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnjzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [OS X v10.5 and later](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnjzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)

### Building Universal

Including the 64-bit architectures, there are currently 4 architectures that can be built:

| Architecture Name | Description |
| --- | --- |
| i386 | Intel (32-bit) |
| ppc | PowerPC (32-bit) |
| ppc64 | PowerPC (64-bit) |
| x86_64 | Intel (64-bit) |

For example, to tell the compiler and linker to build the two 32-bit architectures (which is the customary setting), the following command-line arguments would be used:

```
-arch i386 -arch ppc
```


### Building Perl, Python and Ruby Extensions

The process of building `perl`, `python` and `ruby` extensions is similar to that on other platforms. For `perl`, it looks something like:

```shell
% perl Makefile.PL
% make
% make install
```

For `python`, it looks something like:

```
% python setup.py install
```

And for `ruby`:

```shell
% ruby extconf.rb
% make
% make install
```

All of the arguments to the compiler and linker are automatically generated, and since most other operating systems don’t have the concept of multiple architectures, `perl`, `python` and `ruby` don’t know how to deal with them. It is possible to force additional architecture arguments to be used by the compiler and linker, but it isn’t pretty.

For `perl`, overriding some Makefile variable works in many cases (though is not the only way):

```shell
% perl Makefile.PL
% make PASTHRU_INC='-arch i386 -arch ppc' LD='cc -arch i386 -arch ppc'
% make install
```

Likewise, for `python`, this usually works:

```
% env CFLAGS='-arch i386 -arch ppc' LDFLAGS='-arch i386 -arch ppc' python setup.py install
```

And for `ruby`:

```shell
% env CFLAGS='-arch i386 -arch ppc' LDFLAGS='-arch i386 -arch ppc' ruby extconf.rb
% make
% make install
```


### OS X v10.5 and later

In OS X v10.5 and later, the default for `perl`, `python` and `ruby` extensions is to build the two 32-bit architectures. In most cases, this is what is desired, so there will be no difference in the build procedures.

However, for those times when a different set of architectures is desired, a new environment variable can be used to change this. For example, to build a `perl` extension only for 32-bit PowerPC, you can use:

```shell
% env ARCHFLAGS='-arch ppc' perl Makefile.PL
% make
% make install
```

or for `python`:

```
% env ARCHFLAGS='-arch ppc' python setup.py install
```

or for `ruby`:

```shell
% env ARCHFLAGS='-arch ppc' ruby extconf.rb
% make
% make install
```

> [!NOTE]
> 

Or, you can set the `ARCHFLAGS` environment variable globally, and then just run the normal build/install commands.

> [!NOTE]
> 

> [!NOTE]
> 

> [!NOTE]
> 
