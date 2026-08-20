---
title: Uniform Type Identifiers Reference
apple_id: TP40009257
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreServices
published: '2009-11-17'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Articles/System-DeclaredUniformTypeIdentifiers.html
archived_at: '2026-07-15T08:17:10.461403Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Uniform Type Identifiers Reference](Introduction%20to%20Uniform%20Type%20Identifiers%20Reference.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Uniform%20Type%20Identifiers%20Reference.md)

# System-Declared Uniform Type Identifiers

The following tables list uniform type identifiers (UTIs) that are declared by the system as of OS X v10.4.

Table 1 lists UTIs that are defined by the system.

__Table 1__  System-defined uniform type identifiers

| Identifier (Constant) | Conforms to | Tags | Comments |
| public.item (`kUTTypeItem`) | - |  | Base type for the physical hierarchy. |
| public.content (`kUTTypeContent`) | - |  | Base type for all document content. |
| public.composite-content (`kUTTypeCompositeContent`) | public.content |  | Base type for mixed content. For example, a PDF file contains both text and special formatting data. |
| public.data (`kUTTypeData`) | public.item |  | Base physical type for byte streams (flat files, pasteboard data, and so on). |
| public.database | - |  | Base functional type for databases. |
| public.calendar-event | - |  | Base functional type for scheduled events. |
| public.message (`kUTTypeMessage`) | - |  | Base type for messages (email, IM, and so on). |
| public.presentation | public.composite-content |  | Base type for presentations. |
| public.contact (`kUTTypeContact`) | - |  | Base type for contact information. |
| public.archive (`kUTTypeArchive`) | - |  | Base type for an archive of files and directories. |
| public.disk-image (`kUTTypeDiskImage`) | public.archive |  | Base type for items mountable as a volume. |
| public.text (`kUTTypeText`) | public.content, public.data |  | Base type for all text, including text with markup information (HTML, RTF, and so on). |
| public.plain-text (`kUTTypePlainText`) | public.text | .txt, text/plain | Text of unspecified encoding, with no markup. Equivalent to the MIME type text/plain |
| public.utf8-plain-text (`kUTTypeUTF8PlainText`) | public.plain-text | 'utf8', NSStringPBoardType | Unicode-8 |
| public.utf16-external-plain-​text (`kUTTypeUTF16ExternalPlain​Text`) | public.plain-text | 'ut16' | Unicode-16 with byte-order mark (BOM), or if BOM is not present, an external representation byte order (big-endian). |
| public.utf16-plain-text (`kUTTypeUTF16PlainText`) | public.plain-text | 'utxt' | Unicode-16, native byte order, with an optional byte-order mark (BOM). |
| com.apple.traditional-mac-​plain-text | public.plain-text | 'TEXT' | Classic Mac OS text. |
| public.rtf (`kUTTypeRTF`) | public.text | 'RTF ', .rtf, text/rtf, NeXT Rich Text Format 1.0 pasteboard type, NSRTFPBoardType | Rich Text. |
| com.apple.ink.inktext (`kUTTypeInkText`) | public.data |  | Opaque InkText data. |
| public.html (`kUTTypeHTML`) | public.text | 'HTML', .html, .htm, text/html, Apple HTML pasteboard type | HTML text. |
| public.xml (`kUTTypeXML`) | public.text | .xml, text/xml | XML text. |
| public.source-code (`kUTTypeSourceCode`) | public.plain-text |  | Generic source code. |
| public.c-source (`kUTTypeCSource`) | public.source-code | .c | C source code. |
| public.objective-c-source (`kUTTypeObjectiveCSource`) | public.source-code | .m | Objective-C source code. |
| public.c-plus-plus-source (`kUTTypeCPlusPlusSource`) | public.source-code | .cp, .cpp, .c++, .cc, .cxx | C++ source code. |
| public.objective-c-plus-​plus-source (`kUTTypeObjectiveC​PlusPlusSource`) | public.source-code | .mm | Objective-C++ source code. |
| public.c-header (`kUTTypeCHeader`) | public.source-code | .h | C header file. |
| public.c-plus-plus-header (`kUTTypeCPlusPlusHeader`) | public.source-code | .hpp, .h++ , .hxx | C++ header file. |
| com.sun.java-source (`kUTTypeJavaSource`) | public.source-code | .java, .jav | Java source code |
| public.script | public.source-code |  | Base type for scripting language source code. |
| public.assembly-source | public.source-code | .s | Assembly language source code. |
| com.apple.rez-source | public.source-code | .r | Rez source code. |
| public.mig-source | public.source-code | .defs, .mig | Mig definition source code. |
| com.apple.symbol-export | public.source-code | .exp | Symbol export list. |
| com.netscape.javascript-​source | public.source-code, public.executable | .js, .jscript, .javascript, text/javascript | JavaScript. |
| public.shell-script | public.script | .sh, .command | Shell script. |
| public.csh-script | public.shell-script | .csh | C-shell script. |
| public.perl-script | public.shell-script | .pl, .pm, text/x-perl-script | Perl script. |
| public.python-script | public.shell-script | .py, text/x-python-script | Python script. |
| public.ruby-script | public.shell-script | .rb, .rbw, text/ruby-script | Ruby script. |
| public.php-script | public.shell-script | .php, .php3, .php4, .ph3, .ph4, .phtml, text/x-php-script, text/php, application/php | PHP script. |
| com.sun.java-web-start | public.xml | .jnlp, application/x-java, jnlp-file, application/jnlp | Java web start. |
| com.apple.applescript.text | public.script | .applescript | AppleScript text. |
| com.apple.applescript.​script | public.data | .scpt, 'osas' | AppleScript. |
| public.object-code | public.data, public.executable | .o | Object code. |
| com.apple.mach-o-binary | public.data, public.executable |  | Mach-O binary. |
| com.apple.pef-binary | public.data, public.executable |  | PEF (CFM-based) binary |
| com.microsoft.windows-​executable | public.data, public.executable | .exe, application/x-msdownload | Microsoft Windows application. |
| com.microsoft.windows-​dynamic-link-library | public.data, public.executable | .dll, application/x-msdownload | Microsoft dynamic link library. |
| com.sun.java-class | public.data, public.executable | .class | Java class. |
| com.sun.java-archive | public.data, public.executable, public.archive | .jar , application/java-archive | Java archive. |
| com.apple.quartz-​composer-composition | public.data, public.executable | .qtz , application/x-quartzcomposer | Quartz Composer composition. |
| org.gnu.gnu-tar-archive | public.data, public.archive | .gtar, application/x-gtar | GNU archive. |
| public.tar-archive | org.gnu.gnu-tar-archive | .tar, application/x-tar, application/tar | Tar archive. |
| org.gnu.gnu-zip-archive | public.data, public.archive | .gz, .gzip, application/x-gzip, application/gzip | Gzip archive. |
| org.gnu.gnu-zip-tar-archive | org.gnu.gnu-zip-archve | .tgz | Gzip tar archive. |
| com.apple.binhex-archive | public.data, public.archive | .hqx, application/mac-binhex40, application/mac-binhex, application/binhex | BinHex archive. |
| com.apple.macbinary-​archive | public.data, public.archive | .bin, application/x-macbinary, application/macbinary | MacBinary archive. |
| public.url (`kUTTypeURL`) | public.data | 'url ' | Uniform Resource Locator. |
| public.file-url (`kUTTypeFileURL`) | public.url | 'furl' | File URL. |
| public.url-name | - | 'urln' | URL name. |
| public.vcard (`kUTTypeVCard`) | public.data, public.content | 'vCrd', .vcf, .vcard, text/directory, text/vcard, text/x-vcard, Apple Vcard, pasteboard type | vCard (electronic business card). |
| public.image (`kUTTypeImage`) | public.data, public.content |  | Base type for images. |
| public.fax | public.image |  | Base type for fax images. |
| public.jpeg (`kUTTypeJPEG`) | public.image | 'JPEG', .jpg, .jpeg, image/jpeg | JPEG image. |
| public.jpeg-2000 (`kUTTypeJPEG2000`) | public.image | 'jp2 ', .jp2, image/jp2 | JPEG 2000 image. |
| public.tiff (`kUTTypeTIFF`) | public.image | 'TIFF', .tif, .tiff, image/tiff, NeXT TIFF v4.0 pasteboard type, NSTIFFPBoardType | TIFF image. |
| public.camera-raw-image | public.image |  | Base type for digital camera raw image formats. |
| com.apple.pict (`kUTTypePICT`) | public.image | 'PICT', .pic, .pct, .pict, image/pict, image/x-pict, image/x-macpict | PICT image |
| com.apple.macpaint-image | public.image | .pntg, 'PNTG' | MacPaint image. |
| public.png (`kUTTypePNG`) | public.image | 'PNGf', .png, image/png | PNG image |
| public.xbitmap-image | public.image | .xbm, image/x-quicktime | X bitmap image. |
| com.apple.quicktime-image (`kUTTypeQuickTimeImage`) | public.image | 'qtif', .qif, .qtif, image/x-quicktime | QuickTime image. |
| com.apple.icns (`kUTTypeAppleICNS`) | public.image | 'icns', .icns | Mac OS icon image. |
| com.apple.txn.text-​multimedia-data (`kUTTypeTXNTextAnd​MultimediaData`) | public.data, public.composite-​content | 'txtn' | MLTE (Textension) format for mixed text and multimedia data. |
| public.audiovisual-​content (`kUTTypeAudioVisual​Content`) | public.data, public.content |  | Base type for any audiovisual content. |
| public.movie | public.audiovisual-​content |  | Base type for movies (video with optional audio or other tracks). |
| public.video (`kUTTypeVideo`) | public.movie |  | Base type for video (no audio). |
| com.apple.quicktime-movie (`kUTTypeQuickTimeMovie`) | public.movie | 'MooV', .mov, .qt, video/quicktime | QuickTime movie. |
| public.avi | public.movie | .avi, .vfw, 'Vfw ', video/avi, video/msvideo, video/x-msvideo | AVI movie. |
| public.mpeg (`kUTTypeMPEG`) | public.movie | 'MPG ', 'MPEG', .mpg, .mpeg, .m75, .m15, video/mpg, video/mpeg, video/x-mpg, video/x-mpeg | MPEG-1 or MPEG-2 content. |
| public.mpeg-4 (`kUTTypeMPEG4`) | public.movie | 'mpg4', .mp4, video/mp4, video/mp4v | MPEG-4 content. |
| public.3gpp | public.movie | .3gp, .3gpp, '3gpp', video/3gpp, audio/3gpp | 3GPP movie. |
| public.3gpp2 | public.movie | .3g2 , .3gp2 , '3gp2', video/3gpp2, audio/3gpp2 | 3GPP2 movie. |
| public.audio (`kUTTypeAudio`) | public.audiovisual-​content |  | Base type for audio (no video). |
| public.mp3 (`kUTTypeMP3`) | public.audio | 'MPG3', 'mpg3', 'Mp3 ', 'MP3 ', 'mp3!', 'MP3!', .mp3, audio/mpeg, audio/mpeg3, audio/mpg, audio/mp3, audio/x-mpeg, audio/x-mpeg3, audio/x-mpg, audio/x-mp3 | MPEG-3 audio. |
| public.mpeg-4-audio (`kUTTypeMPEG4Audio`) | public.audio, public.mpeg4 | 'M4A ', .m4a | MPEG-4 audio. |
| com.apple.protected-​mpeg-4-audio (`kUTTypeAppleProtected​MPEG4Audio`) | public.audio | 'M4P ', 'M4B ', .m4p, .m4b | Protected MPEG-4 audio. (iTunes music store format) |
| public.ulaw-audio | public.audio | .au, .ulw, .snd, 'ULAW', audio/basic, audio/au, audio/snd | μLaw audio. |
| public.aifc-audio | public.audio | .aifc, .aiff, .aif, 'AIFC', audio/aiff, audio/x-aiff | AIFF-C audio. |
| public.aiff-audio | public.audio | .aiff, .aif, 'AIFF', audio/aiff, audio/x-aiff | AIFF audio. |
| com.apple.coreaudio-​format | public.audio | .caf, 'caff' | Core Audio format. |
| public.directory (`kUTTypeDirectory`) | public.item |  | Base type for directories. |
| public.folder (`kUTTypeFolder`) | public.directory |  | A plain folder (that is, not a package). |
| public.volume (`kUTTypeVolume`) | public.folder |  | A volume. |
| com.apple.package (`kUTTypePackage`) | public.directory |  | A package (that is, a directory presented to the user as a file). |
| com.apple.bundle (`kUTTypeBundle`) | public.directory | 'BNDL', .bundle | A directory with an internal structure specified by Core Foundation Bundle Services. . |
| public.executable | - |  | Base type for executable data. |
| com.apple.application (`kUTTypeApplication`) | public.executable |  | Base type for applications and other launchable files. |
| com.apple.application-​bundle (`kUTTypeApplicationBundle`) | com.apple.package, com.apple.bundle, com.apple.application | 'APPL', .app | Application bundle. |
| com.apple.application-file (`kUTTypeApplicationFile`) | com.apple.application public.data | 'APPL' | Application file. |
| com.apple.deprecated-​application-file | com.apple.application​-file | 'APPC', 'APPD', 'APPE', 'appe', 'CDEV', 'cdev', 'dfil' | Deprecated application file. |
| com.apple.plugin | com.apple.bundle, com.apple.package | .plugin | Plugin. |
| com.apple.metadata-​importer | com.apple.plugin | .mdimporter | Spotlight importer plugin. |
| com.apple.dashboard-​widget | com.apple.bundle, com.apple.package | .wdgt | Dashboard widget. |
| public.cpio-archive | public.data | .cpio | CPIO archive. |
| com.pkware.zip-archive | public.data, public.archive | .zip, application/zip | Zip archive. |
| com.apple.webarchive (`kUTTypeWebArchive`) | public.data, public.composite-​content |  | Web Kit webarchive format. |
| com.apple.framework (`kUTTypeFramework`) | com.apple.bundle | 'FMWK', .framework | Framework. |
| com.apple.rtfd (`kUTTypeRTFD`) | com.apple.package, public.composite-​content | .rtfd | Rich Text Format Directory. That is, Rich Text with content embedding, on-disk format. |
| com.apple.flat-rtfd (`kUTTypeFlatRTFD`) | public.data, public.composite-​content | NeXT RTFD pasteboard type, NSRTFDPBoardType | Rich Text with content embedding, pasteboard format. |
| com.apple.resolvable (`kUTTypeResolvable`) | - |  | Items that the Alias Manager can resolve. |
| public.symlink (`kUTTypeSymLink`) | public.item, com.apple.resolvable |  | UNIX-style symlink. |
| com.apple.mount-point (`kUTTypeMountPoint`) | public.item, com.apple.resolvable |  | A volume mount point |
| com.apple.alias-record (`kUTTypeAliasRecord`) | public.data, com.apple.resolvable | 'alis' | Alias record. |
| com.apple.alias-file (`kUTTypeAliasFile`) | public.data, com.apple.resolvable |  | Alias file. |
| public.font | public.data |  | Base type for fonts. |
| public.truetype-font | public.font |  | TrueType font. |
| com.adobe.postscript-font | public.font |  | PostScript font. |
| com.apple.truetype-​datafork-suitcase-font | public.truetype-font | .dfont, 'dfon' | TrueType data fork font. |
| public.opentype-font | public.font | .otf, 'OTTO' | PostScript OpenType font. |
| public.truetype-ttf-font | public.truetype-font | .ttf | TrueType OpenType font. |
| public.truetype-collection-​font | public.font | .ttc, 'ttcf' | TrueType collection font. |
| com.apple.font-suitcase | public.font | .suit, 'FFIL', 'ffil', 'sfnt', 'tfil' | Font suitcase. |
| com.adobe.postscript-lwfn​-font | com.adobe.postscript-​font | 'LWFN' | PostScript Type 1 outline font. |
| com.adobe.postscript-pfb-​font | com.adobe.postscript-​font | .pfb | PostScriptType1 outline font. |
| com.adobe.postscript.pfa-​font | com.adobe.postscript-​font | .pfa | PostScriptType 1 outline font. |
| com.apple.colorsync-profile | public.data | .icc, .icm, .pf , 'prof' | ColorSync profile. |

Table 2 lists UTIs used to identify alternate tags. You use these to specify alternate methods of tag identification in UTI declarations.

__Table 2__  Uniform type identifiers for alternate tags

| Identifier | Conforms to | Comments |
| public.filename-extension | public.case-insensitive-text | Filename extension. |
| public.mime-type | public.case-insensitive-text | MIME type. |
| com.apple.ostype | public.text | Four-character code (type `OSType`). |
| com.apple.nspboard-type | public.text | NSPasteboard type. |

Table 3 lists third-party UTIs that the system redeclares as imported types.

__Table 3__  Imported uniform type identifiers

| Identifier (Constant) | Conforms to | Tags | Comments |
| com.adobe.pdf (`kUTTypePDF`) | public.data, public.composite-​content | 'PDF ', .pdf, application/pdf, Apple PDF pasteboard type | PDF data. |
| com.adobe.postscript | public.data | .ps, application/postscript | PostScript data. |
| com.adobe.encapsulated-​postscript | com.adobe.postscript | .eps, NeXT Encapsulated PostScript v1.2 pasteboard type | Encapsulated PostScript. |
| com.adobe.photoshop-​image | public.image | .psd, '8BPS, ' image/x-photoshop, image/photoshop, image/psd, application/photoshop | Adobe Photoshop document. |
| com.adobe.illustrator.ai-​image | public.image | .ai | Adobe Illustrator document. |
| com.compuserve.gif (`kUTTypeGIF`) | public.image | 'GIFf', .gif, image/gif | GIF image. |
| com.microsoft.bmp (`kUTTypeBMP`) | public.image | 'BMP ', 'BMPf', .bmp | Windows bitmap image. |
| com.microsoft.ico (`kUTTypeICO`) | public.image | .ico | Windows icon image. |
| com.microsoft.word.doc | public.data | 'W8BN', .doc, application/msword | Microsoft Word data. |
| com.microsoft.excel.xls | public.data | 'XLS8', .xls, application/vnd.ms-excel | Microsoft Excel data. |
| com.microsoft.powerpoint.​ppt | public.data, public.presentation | .ppt, 'SLD8', application/mspowerpoint | Microsoft PowerPoint presentation. |
| com.microsoft.waveform-​audio | public.audio | .wav, .wave, '.WAV', 'WAVE', audio/wav, audio/wave | Waveform audio. |
| com.microsoft.advanced-​systems-format | public.audiovisual-​content | .asf , 'ASF_', video/x-ms-asf | Microsoft Advanced Systems format. |
| com.microsoft.windows-​media-wm | public.movie, com.microsoft.advanced-​systems-format | .wm, video/x-ms-wm | Windows media. |
| com.microsoft.windows-​media-wmv | public.movie, com.microsoft.advanced-​systems-format | .wmv, video/x-ms-wmv | Windows media. |
| com.microsoft.windows-​media-wmp | public.movie, com.microsoft.advanced-​systems-format | .wmp, video/x-ms-wmp | Windows media. |
| com.microsoft.windows-​media-wma | public.audio, com.microsoft.advanced-​systems-format | .wma, video/x-ms-wma | Windows media audio. |
| com.microsoft.advanced-​stream-redirector | public.xml, public.audiovisual-​content | .asx, 'ASX_', video/x-ms-asx | Advanced Stream Redirector. |
| com.microsoft.windows-​media-wmx | public.audio, com.microsoft.advanced-​stream-redirector | .wmx , video-x-ms-wmx | Windows media. |
| com.microsoft.windows-​media-wvx | public.audio, com.microsoft.advanced-​stream-redirector | .wvx, video-x-ms-wvx | Windows media. |
| com.microsoft.windows-​media-wax | public.audio, com.microsoft.advanced-​stream-redirector | .wax, video-x-ms-wax | Windows media audio. |
| com.apple.keynote.key | com.apple.package, public.presentation | .key | Apple Keynote document. |
| com.apple.keynote.kth | com.apple.package, public.composite-​content | .kth | Apple Keynote theme. |
| com.truevision.tga-image | public.image | .tga, 'TPIC', image/targa, image/tga, application/tga | TGA image. |
| com.sgi.sgi-image | public.image | .sgi, '.SGI', image/sgi | Silicon Graphics image. |
| com.ilm.openexr-image | public.image | .exr | OpenEXR image. |
| com.kodak.flashpix.image | public.image | .fpx, image/fpx, application/vnd.fpx | FlashPix image. |
| com.j2.jfx-fax | public.fax | .jfx | J2 fax. |
| com.js.efx-fax | public.fax | .efx, image/efax | eFax fax. |
| com.digidesign.sd2-audio | public.audio | .sd2, 'Sd2f' | Digidesign Sound Designer II audio. |
| com.real.realmedia | public.movie | .rm, 'PNRM', application/vnd.rn-realmedia | RealMedia. |
| com.real.realaudio | public.audio | .ram, .ra , 'PNRA', audio/vnd.rn-realaudio, audio/x-pn-realaudio | RealMedia audio. |
| com.real.smil | public.xml | .smil, application/smil | Real synchronized multimedia integration language. |
| com.allume.stuffit-archive | public.data, public.archive | .sit, .sitx, application/x-stuffit, application/x-sit , application/stuffit | Stuffit archive. |

[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Uniform%20Type%20Identifiers%20Reference.md)

