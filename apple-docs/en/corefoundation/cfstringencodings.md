---
title: CFStringEncodings
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringencodings
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringencodings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringencodings.json'
content_hash: 'sha256:273fecd011f09d92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringEncodings

<sub>Enumeration</sub>

Index type for constants used to specify external string encodings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFStringEncodings
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [kCFStringEncodingANSEL](cfstringencodings/ansel.md) — ANSEL (ANSI Z39.47).
- [kCFStringEncodingBig5](cfstringencodings/big5.md) — Big-5 (has variants)
- [kCFStringEncodingBig5_E](cfstringencodings/big5_e.md) — Taiwan Big-5E standard.
- [kCFStringEncodingBig5_HKSCS_1999](cfstringencodings/big5_hkscs_1999.md) — Big-5 with Hong Kong special char set supplement.
- [kCFStringEncodingCNS_11643_92_P1](cfstringencodings/cns_11643_92_p1.md) — CNS 11643-1992 plane 1.
- [kCFStringEncodingCNS_11643_92_P2](cfstringencodings/cns_11643_92_p2.md) — CNS 11643-1992 plane 2.
- [kCFStringEncodingCNS_11643_92_P3](cfstringencodings/cns_11643_92_p3.md) — CNS 11643-1992 plane 3 (was plane 14 in 1986 version).
- [kCFStringEncodingDOSArabic](cfstringencodings/dosarabic.md) — Code page 864.
- [kCFStringEncodingDOSBalticRim](cfstringencodings/dosbalticrim.md) — Code page 775.
- [kCFStringEncodingDOSCanadianFrench](cfstringencodings/doscanadianfrench.md) — Code page 863.
- [kCFStringEncodingDOSChineseSimplif](cfstringencodings/doschinesesimplif.md) — Code page 936, also for Windows.
- [kCFStringEncodingDOSChineseTrad](cfstringencodings/doschinesetrad.md) — Code page 950, also for Windows.
- [kCFStringEncodingDOSCyrillic](cfstringencodings/doscyrillic.md) — Code page 855, IBM Cyrillic.
- [kCFStringEncodingDOSGreek](cfstringencodings/dosgreek.md) — Code page 737 (formerly code page 437G).
- [kCFStringEncodingDOSGreek1](cfstringencodings/dosgreek1.md) — Code page 851.
- [kCFStringEncodingDOSGreek2](cfstringencodings/dosgreek2.md) — Code page 869, IBM Modern Greek.
- [kCFStringEncodingDOSHebrew](cfstringencodings/doshebrew.md) — Code page 862.
- [kCFStringEncodingDOSIcelandic](cfstringencodings/dosicelandic.md) — Code page 861.
- [kCFStringEncodingDOSJapanese](cfstringencodings/dosjapanese.md) — Code page 932, also for Windows.
- [kCFStringEncodingDOSKorean](cfstringencodings/doskorean.md) — Code page 949, also for Windows; Unified Hangul Code.
- [kCFStringEncodingDOSLatin1](cfstringencodings/doslatin1.md) — Code page 850, “Multilingual”.
- [kCFStringEncodingDOSLatin2](cfstringencodings/doslatin2.md) — Code page 852, Slavic.
- [kCFStringEncodingDOSLatinUS](cfstringencodings/doslatinus.md) — Code page 437.
- [kCFStringEncodingDOSNordic](cfstringencodings/dosnordic.md) — Code page 865.
- [kCFStringEncodingDOSPortuguese](cfstringencodings/dosportuguese.md) — Code page 860.
- [kCFStringEncodingDOSRussian](cfstringencodings/dosrussian.md) — Code page 866.
- [kCFStringEncodingDOSThai](cfstringencodings/dosthai.md) — Code page 874, also for Windows.
- [kCFStringEncodingDOSTurkish](cfstringencodings/dosturkish.md) — Code page 857, IBM Turkish.
- [kCFStringEncodingEBCDIC_CP037](cfstringencodings/ebcdic_cp037.md) — code page 037, extended EBCDIC (Latin-1 set) for US, Canada.
- [kCFStringEncodingEBCDIC_US](cfstringencodings/ebcdic_us.md) — basic EBCDIC-US
- [kCFStringEncodingEUC_CN](cfstringencodings/euc_cn.md) — ISO 646, GB 2312-80.
- [kCFStringEncodingEUC_JP](cfstringencodings/euc_jp.md) — ISO 646, 1-byte katakana, JIS 208, JIS 212.
- [kCFStringEncodingEUC_KR](cfstringencodings/euc_kr.md) — ISO 646, KS C 5601-1987.
- [kCFStringEncodingEUC_TW](cfstringencodings/euc_tw.md) — ISO 646, CNS 11643-1992 Planes 1-16.
- [kCFStringEncodingGBK_95](cfstringencodings/gbk_95.md) — Annex to GB 13000-93; for Windows 95.
- [kCFStringEncodingGB_18030_2000](cfstringencodings/gb_18030_2000.md)
- [kCFStringEncodingGB_2312_80](cfstringencodings/gb_2312_80.md)
- [kCFStringEncodingHZ_GB_2312](cfstringencodings/hz_gb_2312.md) — HZ (RFC 1842, for Chinese mail & news).
- [kCFStringEncodingISOLatin10](cfstringencodings/isolatin10.md) — ISO 8859-16.
- [kCFStringEncodingISOLatin2](cfstringencodings/isolatin2.md) — ISO 8859-2.
- [kCFStringEncodingISOLatin3](cfstringencodings/isolatin3.md) — ISO 8859-3.
- [kCFStringEncodingISOLatin4](cfstringencodings/isolatin4.md) — ISO 8859-4.
- [kCFStringEncodingISOLatin5](cfstringencodings/isolatin5.md) — ISO 8859-9.
- [kCFStringEncodingISOLatin6](cfstringencodings/isolatin6.md) — ISO 8859-10.
- [kCFStringEncodingISOLatin7](cfstringencodings/isolatin7.md) — ISO 8859-13.
- [kCFStringEncodingISOLatin8](cfstringencodings/isolatin8.md) — ISO 8859-14.
- [kCFStringEncodingISOLatin9](cfstringencodings/isolatin9.md) — ISO 8859-15.
- [kCFStringEncodingISOLatinArabic](cfstringencodings/isolatinarabic.md) — ISO 8859-6, =ASMO 708, =DOS CP 708.
- [kCFStringEncodingISOLatinCyrillic](cfstringencodings/isolatincyrillic.md) — ISO 8859-5.
- [kCFStringEncodingISOLatinGreek](cfstringencodings/isolatingreek.md) — ISO 8859-7.
- [kCFStringEncodingISOLatinHebrew](cfstringencodings/isolatinhebrew.md) — ISO 8859-8.
- [kCFStringEncodingISOLatinThai](cfstringencodings/isolatinthai.md) — ISO 8859-11.
- [kCFStringEncodingISO_2022_CN](cfstringencodings/iso_2022_cn.md)
- [kCFStringEncodingISO_2022_CN_EXT](cfstringencodings/iso_2022_cn_ext.md)
- [kCFStringEncodingISO_2022_JP](cfstringencodings/iso_2022_jp.md)
- [kCFStringEncodingISO_2022_JP_1](cfstringencodings/iso_2022_jp_1.md) — RFC 2237.
- [kCFStringEncodingISO_2022_JP_2](cfstringencodings/iso_2022_jp_2.md)
- [kCFStringEncodingISO_2022_JP_3](cfstringencodings/iso_2022_jp_3.md) — JIS X0213.
- [kCFStringEncodingISO_2022_KR](cfstringencodings/iso_2022_kr.md)
- [kCFStringEncodingJIS_C6226_78](cfstringencodings/jis_c6226_78.md)
- [kCFStringEncodingJIS_X0201_76](cfstringencodings/jis_x0201_76.md)
- [kCFStringEncodingJIS_X0208_83](cfstringencodings/jis_x0208_83.md)
- [kCFStringEncodingJIS_X0208_90](cfstringencodings/jis_x0208_90.md)
- [kCFStringEncodingJIS_X0212_90](cfstringencodings/jis_x0212_90.md)
- [kCFStringEncodingKOI8_R](cfstringencodings/koi8_r.md) — Russian internet standard.
- [kCFStringEncodingKOI8_U](cfstringencodings/koi8_u.md) — RFC 2319, Ukrainian.
- [kCFStringEncodingKSC_5601_87](cfstringencodings/ksc_5601_87.md) — Same as KSC 5601-92 without Johab annex.
- [kCFStringEncodingKSC_5601_92_Johab](cfstringencodings/ksc_5601_92_johab.md) — KSC 5601-92 Johab annex.
- [kCFStringEncodingMacArabic](cfstringencodings/macarabic.md)
- [kCFStringEncodingMacArmenian](cfstringencodings/macarmenian.md)
- [kCFStringEncodingMacBengali](cfstringencodings/macbengali.md)
- [kCFStringEncodingMacBurmese](cfstringencodings/macburmese.md)
- [kCFStringEncodingMacCeltic](cfstringencodings/macceltic.md)
- [kCFStringEncodingMacCentralEurRoman](cfstringencodings/maccentraleurroman.md)
- [kCFStringEncodingMacChineseSimp](cfstringencodings/macchinesesimp.md)
- [kCFStringEncodingMacChineseTrad](cfstringencodings/macchinesetrad.md)
- [kCFStringEncodingMacCroatian](cfstringencodings/maccroatian.md)
- [kCFStringEncodingMacCyrillic](cfstringencodings/maccyrillic.md)
- [kCFStringEncodingMacDevanagari](cfstringencodings/macdevanagari.md)
- [kCFStringEncodingMacDingbats](cfstringencodings/macdingbats.md)
- [kCFStringEncodingMacEthiopic](cfstringencodings/macethiopic.md)
- [kCFStringEncodingMacExtArabic](cfstringencodings/macextarabic.md)
- [kCFStringEncodingMacFarsi](cfstringencodings/macfarsi.md) — Like MacArabic but uses Farsi digits.
- [kCFStringEncodingMacGaelic](cfstringencodings/macgaelic.md)
- [kCFStringEncodingMacGeorgian](cfstringencodings/macgeorgian.md)
- [kCFStringEncodingMacGreek](cfstringencodings/macgreek.md)
- [kCFStringEncodingMacGujarati](cfstringencodings/macgujarati.md)
- [kCFStringEncodingMacGurmukhi](cfstringencodings/macgurmukhi.md)
- [kCFStringEncodingMacHFS](cfstringencodings/machfs.md) — Meta-value, should never appear in a table.
- [kCFStringEncodingMacHebrew](cfstringencodings/machebrew.md)
- [kCFStringEncodingMacIcelandic](cfstringencodings/macicelandic.md)
- [kCFStringEncodingMacInuit](cfstringencodings/macinuit.md)
- [kCFStringEncodingMacJapanese](cfstringencodings/macjapanese.md)
- [kCFStringEncodingMacKannada](cfstringencodings/mackannada.md)
- [kCFStringEncodingMacKhmer](cfstringencodings/mackhmer.md)
- [kCFStringEncodingMacKorean](cfstringencodings/mackorean.md)
- [kCFStringEncodingMacLaotian](cfstringencodings/maclaotian.md)
- [kCFStringEncodingMacMalayalam](cfstringencodings/macmalayalam.md)
- [kCFStringEncodingMacMongolian](cfstringencodings/macmongolian.md)
- [kCFStringEncodingMacOriya](cfstringencodings/macoriya.md)
- [kCFStringEncodingMacRomanLatin1](cfstringencodings/macromanlatin1.md) — Mac OS Roman permuted to align with ISO Latin-1.
- [kCFStringEncodingMacRomanian](cfstringencodings/macromanian.md)
- [kCFStringEncodingMacSinhalese](cfstringencodings/macsinhalese.md)
- [kCFStringEncodingMacSymbol](cfstringencodings/macsymbol.md)
- [kCFStringEncodingMacTamil](cfstringencodings/mactamil.md)
- [kCFStringEncodingMacTelugu](cfstringencodings/mactelugu.md)
- [kCFStringEncodingMacThai](cfstringencodings/macthai.md)
- [kCFStringEncodingMacTibetan](cfstringencodings/mactibetan.md)
- [kCFStringEncodingMacTurkish](cfstringencodings/macturkish.md)
- [kCFStringEncodingMacUkrainian](cfstringencodings/macukrainian.md)
- [kCFStringEncodingMacVT100](cfstringencodings/macvt100.md) — VT100102 font from Comm Toolbox: Latin-1 repertoire + box drawing etc.
- [kCFStringEncodingMacVietnamese](cfstringencodings/macvietnamese.md)
- [kCFStringEncodingNextStepJapanese](cfstringencodings/nextstepjapanese.md) — NextStep Japanese encoding.
- [kCFStringEncodingShiftJIS](cfstringencodings/shiftjis.md) — Plain Shift-JIS.
- [kCFStringEncodingShiftJIS_X0213](cfstringencodings/shiftjis_x0213.md) — Shift-JIS format encoding of JIS X0213 planes 1 and 2.
- [kCFStringEncodingShiftJIS_X0213_MenKuTen](cfstringencodings/shiftjis_x0213_menkuten.md) — JIS X0213 in plane-row-column notation.
- [kCFStringEncodingUTF7](cfstringencodings/utf7.md) — kTextEncodingUnicodeDefault + kUnicodeUTF7Format RFC2152.
- [kCFStringEncodingUTF7_IMAP](cfstringencodings/utf7_imap.md) — UTF-7 (IMAP folder variant) RFC3501.
- [kCFStringEncodingVISCII](cfstringencodings/viscii.md) — RFC 1456, Vietnamese.
- [kCFStringEncodingWindowsArabic](cfstringencodings/windowsarabic.md) — Code page 1256.
- [kCFStringEncodingWindowsBalticRim](cfstringencodings/windowsbalticrim.md) — Code page 1257.
- [kCFStringEncodingWindowsCyrillic](cfstringencodings/windowscyrillic.md) — Code page 1251, Slavic Cyrillic.
- [kCFStringEncodingWindowsGreek](cfstringencodings/windowsgreek.md) — Code page 1253.
- [kCFStringEncodingWindowsHebrew](cfstringencodings/windowshebrew.md) — Code page 1255.
- [kCFStringEncodingWindowsKoreanJohab](cfstringencodings/windowskoreanjohab.md) — Code page 1361, for Windows NT.
- [kCFStringEncodingWindowsLatin2](cfstringencodings/windowslatin2.md) — Code page 1250, Central Europe.
- [kCFStringEncodingWindowsLatin5](cfstringencodings/windowslatin5.md) — Code page 1254, Turkish.
- [kCFStringEncodingWindowsVietnamese](cfstringencodings/windowsvietnamese.md) — Code page 1258.

### Initializers

- [init(rawValue:)](<cfstringencodings/init(rawvalue_).md>)

### Type Properties

- [kCFStringEncodingShiftJIS_X0213_00](cfstringencodings/shiftjis_x0213_00.md) — Shift-JIS format encoding of JIS X0213 planes 1 and 2. _(deprecated)_

## See Also

### Data Types

- [CFStringEncoding](cfstringencoding.md) — An integer type for constants used to specify supported string encodings in various CFString functions.
- [CFStringCompareFlags](cfstringcompareflags.md) — A [CFOptionFlags](cfoptionflags.md) type for specifying options for string comparison .
- [CFStringInlineBuffer](cfstringinlinebuffer.md) — Defines the buffer and related fields used for in-line buffer access of characters in CFString objects.
