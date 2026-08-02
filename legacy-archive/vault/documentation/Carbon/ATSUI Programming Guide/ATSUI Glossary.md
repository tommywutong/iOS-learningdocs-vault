---
title: ATSUI Programming Guide
apple_id: TP30000984
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-09-30'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ATSUI_Concepts/atsui_glossary/atsui_glossary.html
archived_at: '2026-07-15T05:22:24.630007Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [ATSUI Programming Guide](Introduction%20to%20ATSUI%20Programming%20Guide.md)


[Previous](Document%20Revision%20History.md)

# ATSUI Glossary

- __absolute position__

  A specific position, given in coordinates, for the origin of each character or glyph in a line of text. Compare [relative position](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjbcuqskb).

- __active end__

  When selecting text, the point at which the user releases the mouse button. See also [anchor point](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjfdekr2g).

- __advance delta__

  The distance between the end of one glyph’s advance and the next glyph’s real position.

- __advance height__

  The distance from the top of a glyph to the bottom of the glyph, including the top-side bearing and bottom-side bearing.

- __advance width__

  The full horizontal width of a glyph as measured from its origin to the origin of the next glyph on the line, including the side bearings on both sides.

- __alignment__

  The process of placing text in relation to one or both margins. Also referred to as flushness.

- __anchor point__

  The position in the text at which the user positions the pointer and presses the mouse button. See also [active end](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscirbucskf).

- __angled caret__

  A caret whose angle in relation to the baseline of the display text is equivalent to the slant of the glyphs making up the text.

- __anti-aliasing__

  The smoothing of jagged edges on a displayed glyph by modifying the transparencies of individual pixels along the glyph’s edge.

- __ascent line__

  An imaginary horizontal line that corresponds approximately to the tops of the uppercase letters in the font. Uppercase letters are chosen because, among the regularly used glyphs in a font, these are generally the tallest.

- __backing store__

  A file in which the Virtual Memory Manager stores the contents of unneeded pages of memory.

- __baseline__

  An imaginary line used to align glyphs in a line of text.

- __baseline delta__

  The distance (in points) between a baseline and y = 0; sometimes referred to as delta-y. See also [baseline type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscirbegrsf).

- __baseline type__

  The classification of baseline used with a particular kind of text. See, for example, [Roman baseline](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscirfesrkh).

- __Bézier curve__

  A cubic equation originally developed by Pierre Bézier. In typography, used to define the shape of a glyph.

- __bidi__

  See [bidirectional script system](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugssci5beossh).

- __bidirectional script system__

  A script system in which text is generally right-aligned with most characters written from right to left, but with some left-to-right text as well. Arabic and Hebrew are bidirectional script systems.

- __blit__

  Slang for copying an image from memory to the screen.

- __bottom-side bearing__

  The white space between the bottom of the glyph and the visible ending of the glyph.

- __bounding box__

  The smallest rectangle that entirely encloses the pixels or outline of a glyph.

- __byte offset__

  The numbering of character codes in source text. Compare [edge offset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjjcugrkc).

- __caret__

  A vertical or slanted blinking bar, appearing at a caret position in the display text, that marks the point at which text is to be inserted or deleted. Compare [dual caret](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugssci5auqrki).

- __caret angle__

  The angle of a caret or of the edges of a highlight. The caret angle can be perpendicular to the baseline or parallel to the angle of the style run’s text.

- __caret position__

  A location on screen, typically between glyphs, that relates directly to a caret offset in the source text.

- __caret type__

  A designation of the behavior of the caret at direction boundaries in text. See also [dual caret](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugssci5auqrki).

- __character__

  A symbol standing for a sound, syllable, or notion used in writing; one of the simple elements of a written language, for example, the lowercase letter “a” or the number “1”. Compare [character code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjjcuirsj), [glyph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscirfeiqsc).

- __character clusters__

  A collection of characters treated as individual components of a whole, including a principal character plus attachments in memory. For example, in Hebrew, a cluster may be composed of a consonant, a vowel, a dot to soften the pronunciation of the consonant, and a cantillation mark.

- __character code__

  A numerical representation of a character. Each writing system or language has one or more character encodings—tables that relate character codes to the characters they represent.

- __character encoding__

  An internal conversion table for interpreting a specific character set.

- __contextual features__

  Features that are applied to a glyph depending on the glyph’s position relative to adjacent glyphs. Compare [noncontextual features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscizdeurcf).

- __contextual form__

  An alternate form of a glyph whose use depends on the glyph’s placement in a word.

- __contiguous highlighting__

  Highlighting that consists of a single, contiguous shape across direction boundaries, even when it does not exactly match the selection range to which it corresponds. Compare [discontinuous highlighting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjfauursb).

- __counter__

  The oval in glyphs such as “p” or “d”.

- __cross-stream kerning__

  The automatic movement of glyphs perpendicular to the line orientation of the text.

- __cross-stream shift__

  A type of positional shift that applies equally to all glyphs in a style run by raising or lowering the entire style run (or shifts it sideways if it’s vertical text). Compare [with-stream shift](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjjbuuqsg).

- __cubic curve__

  A curve defined by a cubic equation. See also [Bï¿½zier curve](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscincueq2c).

- __cursor__

  A small icon, often an arrow or an I-beam shape, that moves with the mouse or other pointing device. Compare [caret](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjjfegq2g).

- __descent line__

  An imaginary horizontal line that usually corresponds with the bottoms of the descenders in a font. The descent line is the same distance from the baseline for all glyphs in the font, whether or not they have descenders.

- __device delta__

  A value used to adjust truncated factional values for cases in which fractional positioning can’t be used; for example, to compensate for integer drawing in QuickDraw. Device delta values are usually used when anti-aliasing is turned off. However, these values can be used when anti-aliasing is on, to assure that the glyphs in a connected script (such as one that uses the Zapfino font) are connected smoothly.

- __device advance__

  The number of pixels of the advance for the glyph as actually drawn on the screen.

- __device space__

  The coordinate system that defines the position and scale (pixel size) of a specific view device.

- __diacritical marks__

  A mark, such as an accent, that is used in conjunction with a character to indicate phonetic value.

- __direct-access functions__

  ATSUI functions that allow you to manipulate glyph data directly.

- __direction boundary__

  A point, between offsets in memory or glyphs in a display, at which the direction of stored or displayed text changes.

- __discontinuous highlighting__

  Highlighting that exactly matches the selection range it corresponds to. It may consist of discontinuous areas when the selection range crosses direction boundaries. Compare [contiguous highlighting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscizdemrsc).

- __display order__

  The left-to-right order in which ATSUI displays glyphs. Display order determines the glyph index of each glyph in a line and may differ from the input order of the text. Compare [input order](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjbdegqsi).

- __display text__

  The visual representation of the text of a text layout object. Display text consists of a sequence of glyphs, arranged in display order. Compare [source text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscineegski).

- __drop capital__

  A large uppercase letter that drops below the main line of text for aesthetic reasons.

- __dual caret__

  A type of caret that, at the boundary between text of opposite directions, divides into two parts: a high caret and a low caret, each measuring half the line’s height. The two separate half-carets merge into one in unidirectional text.

- __edge offset__

  A byte offset into the source text associated with a text layout object that specifies a position between byte values. Edge offsets in source text are related to caret positions in display text. Compare [byte offset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscijduercd).

- __exclusive feature type__

  A feature for which you can choose only one of the available feature selectors, such as whether numbers are to be proportional or fixed-width. Compare [nonexclusive feature type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscizceqr2e).

- __feature selectors__

  A means of defining particular font features in a feature type. See also [feature type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscizduqqkh).

- __feature type__

  A group of font features in a style object that are applied to each style run based on font defaults. See also [feature selectors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjjdeuscf).

- __flushness__

  See [alignment](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscijbusssf).

- __font__

  A collection of glyphs that usually have some element of design consistency such as the shapes of the counters, the design of the stem, stroke thickness, or the use of serifs.

- __font family__

  A group of fonts that share certain characteristics and a common family name.

- __font features__

  The set of typographic and layout capabilities that create a specific appearance for the text associated with a text layout object.

- __font ID__

  A value that identifies a font to the font management system. The font ID is assigned to a font at system startup; the specific value does not persist across system startups.

- __font instance__

  A setting identified by the font’s designer that matches specific values along the available variation axes and gives those values a name.

- __font name__

  A set of specific information in a font object about a font, such as its family name, style, copyright date, version, and manufacturer. Some font names are used to build menus in an application, whereas other names are used to identify the font uniquely.

- __font variation__

  An algorithmic way to produce a range of typestyles along a particular variation axis.

- __glyph__

  The distinct visual representation of a character in a form that a screen or printer can display. A glyph may represent one character (the lowercase a), more than one character (the fi ligature), part of a character (the dot over an i), or a nonprinting character (the space character). See also [character](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscivcuescg).

- __glyph code__

  A number that specifies a particular glyph in a font. Fonts map character codes to glyph codes, which in turn specify individual glyphs.

- __glyph direction__

  The direction in which successive glyphs are read.

- __glyph index__

  The order of a glyph in a line of display text. The leftmost glyph in a line of text has a glyph index of 0; each succeeding glyph to the right has an index one greater than the previous glyph. Compare [edge offset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjjcugrkc).

- __glyph orientation__

  A value that specifies which direction (vertical or horizontal) glyphs should be drawn.

- __glyph origin__

  The point used to position a glyph when drawing.

- __glyph outline__

  The curves that make up the shape of the glyph.

- __hanging baseline__

  The baseline used by Devanagari and similar scripts, where most of the glyph is below the baseline.

- __hanging glyphs__

  A set of glyphs, usually punctuation, that typically extend beyond the left and right margins of the text area and whose widths are not counted when line length is measured.

- __Hangul__

  A Korean subscript that consists of blocks of component glyphs called Jamo that are characters different from typical character clusters in that they are treated as singular units in memory; there are no principal characters and attachments.

- __highlighting__

  The display of text in inverse video or with a colored background. Highlighting in display text corresponds to a selection range in source text.

- __hints__

  Information provided with a font that can be used to scale glyphs to various sizes.

- __hit-testing__

  The process of converting a location within a line of display text into a caret offset in the source text of that line.

- __hyphenation point__

  An entry in an array of edge offsets in the source text at which it is appropriate to break a line of display text.

- __ideal metrics__

  Resolution-independent measurements used to describe how a glyph is drawn. Compare [screen metrics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjjcemq2i).

- __image bounding rectangle__

  The smallest rectangle that completely encloses the filled or framed parts of a block of text. See also [typographic bounding rectangle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewueqkkizfegscc).

- __imposed width__

  A control feature that forces a specific width onto the glyphs of a style run, regardless of its text content or other style properties.

- __index__

  See [glyph index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscindeiq2c).

- __input order__

  The order in which characters are written or entered from a keyboard. The input order of a line of text can differ from its display order. Compare [display order](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjjeeuskd).

- __insertion point__

  The point in the source text at which text is to be inserted or deleted. An insertion point is specified by a single caret position. Compare [caret position](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjbbeiski).

- __Jamo__

  An individual phonetic glyph in the Korean script that is transformed and combined into clusters called Hangul.

- __justification__

  The process of typographically expanding or compressing a line of text to fit a text width.

- __justification gap__

  The difference in the length of a line before and after justification.

- __justification override__

  The degree to which ATSUI should override justification behavior for glyphs in a style run.

- __justification priority__

  The priority order in which classes of glyphs are processed during justification.

- __kashida__

  An extension-bar glyph that is added to certain Arabic glyphs during justification.

- __kerning__

  An adjustment to the normal spacing that occurs between two or more specifically named glyphs, known as the kerning pair.

- __kerning pair__

  Two specifically named glyphs that are kerned together by a set amount. See also [kerning](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjbfeesse).

- __language__

  The written and spoken methods of combining words to create meaning used by a particular group of people.

- __Last Resort font__

  A collection of glyphs that represent types of Unicode characters. These glyphs can be used as a backup to any other font; if the font cannot represent any particular Unicode character, the appropriate “missing” glyph from the Last Resort font can be used instead.

- __layout cache__

  A cache that contains all the information ATSUI needs to draw a range of text associated with a text layout object. This includes caret positions, the memory locations of glyphs, and other information needed to lay out the glyphs.

- __leading edge__

  The edge of a glyph that is encountered first when reading text of that glyph’s language. For glyphs of left-to-right text, the leading edge is the left edge; for glyphs of right-to-left text, the leading edge is the right edge.

- __left-side bearing__

  The white space between the glyph origin and the visible beginning of the glyph.

- __ligature__

  Two or more glyphs connected to form a single new glyph.

- __ligature decomposition__

  The breaking up of a ligature into its component glyphs during justification so that the individual glyphs may more evenly occupy the space allotted to the ligature.

- __ligature splitting__

  The division of a ligature for hit-testing purposes into regions corresponding to each of its component glyphs.

- __line breaking__

  The process of determining the proper location at which to truncate a line of text so that it fits within a given text width.

- __line and layout attributes__

  Attributes that specify how the lines of text associated with the text layout object are displayed and formatted. Line attributes control an individual line of text; layout attributes control all of the text associated with a text layout object.

- __line direction__

  The overall direction in which a line of text is read. The line direction is the lowest nested level of dominant direction on a line.

- __line length__

  The distance, in points, from the origin of the first glyph on a line through the advance width of the last glyph.

- __margins__

  The left, right, top, and bottom sides of the text area.

- __metamorphosis__

  The process by which glyphs are rearranged, substituted, deleted, and inserted based upon their properties and contextual states.

- __native curve type__

  The curve type—cubic or quadratic—used by a font designer to specify a font.

- __negative justification__

  A layout in which the glyphs on a line do not naturally fit within the line width set by the developer.

- __noncontextual features__

  Features that are applied in the same manner to a glyph regardless of the adjacent glyphs. See also [contextual features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjfeugrsk).

- __nonexclusive feature type__

  A feature for which you can enable any number of feature selectors at once. Compare [exclusive feature type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscinbegrsj).

- __offsets__

  Monotonically increasing or decreasing values. In ATSUI, offsets are in `Unichars` units and are typically used to specify starting and ending points for a string of text.

- __optical alignment__

  The fine adjustment of glyph positions at the ends of lines to give a more even visual appearance to margins.

- __point size__

  The size of a font’s glyphs as measured from the baseline of one line of text to the baseline of the next line of single-spaced text. In the United States, point size is measured in typographic points.

- __postcompensation action__

  The extra processing, such as addition of kashidas and ligature decomposition, that occurs after glyphs have been repositioned during justification.

- __quadratic curve__

  A curve specified by a quadratic equation.

- __real position__

  The actual drawing position on the x-axis for the origin of each character or glyph in a line of text given in coordinates relative to the preceding character or glyph.

- __relative position__

  A position for the origin of each character or glyph in a line of text given in coordinates relative to the preceding character or glyph. Compare [absolute position](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscirausr2k).

- __right-side bearing__

  The white space on the right side of the glyph; this value may or may not be equal to the value of the left-side bearing.

- __Roman baseline__

  The baseline used in most Roman scripts and in Arabic and Hebrew.

- __ruby text__

  Text usually used to provide annotations or indicate pronunciation for Asian languages. Ruby text is displayed using a smaller font size than the text it annotates.

- __run__

  A sequence of glyphs that are contiguous in memory and share a set of common attributes.

- __screen metrics__

  Resolution-dependent measurements used to describe how a glyph is drawn. Compare [ideal metrics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjjeuissd).

- __script__

  A method for depicting words visually.

- __selection range__

  The contiguous sequence of characters in the source text that mark where the next editing operation is to occur. The glyphs corresponding to those characters are commonly highlighted on screen.

- __serif__

  The fine lines stemming from and at an angle to the upper and lower ends of the main strokes of a letter—for example, the little “feet” on the bottom of the vertical strokes in the uppercase letter “M” in Times Roman typeface.

- __smart swash__

  A variation of an existing glyph (often ornamental) that is contextual. Compare [swash](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscivbusqkj).

- __source text__

  A stored sequence of character codes that represents a line of text. Characters in source text are stored in input order. Compare [display text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscizdeussb).

- __split caret__

  See [dual caret](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugssci5auqrki).

- __storage order__

  See [input order](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjbdegqsi), [display order](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjjeeuskd).

- __style run__

  A sequence of glyphs (contiguous in memory backing store) that share the same style.

- __surrogates__

  Values that allow additional characters to be mapped to the Unicode 16-bit character set.

- __swash__

  A variation of an existing glyph (often ornamental) that is noncontextual. Compare [smart swash](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscircekqsd).

- __style attributes__

  A collection of values and settings that override the font-specified behavior for displaying and formatting text in a style run.

- __style object__

  An opaque object that contains a collection of stylistic attributes. Style objects can be applied to runs within a text layout object.

- __text__

  A set of specific symbols that, when displayed in a meaningful order, conveys information.

- __text area__

  The space on the display device within which the text should fit.

- __text direction__

  The direction in which reading proceeds. Roman text has a left-to-right direction; Hebrew and Arabic have a (predominantly) right-to-left direction; Chinese and Japanese can have a vertical direction.

- __text face__

  An algorithmic way for your application to produce typestyles.

- __text layout object__

  An opaque object that contains information to control the display and formatting of the text to which the object is associated.

- __text run__

  A complete unit of text made up of character codes or glyph codes.

- __text styles__

  The visual attributes, other than size, applied as a systematic variation to the plain (unstyled) characteristics of a font’s glyphs. Some typical text styles include plain, bold, italic, underline, outline, shadow, condensed, and extended.

- __text width__

  The area between the margins; it is the length available for displaying a line of text.

- __top-side bearing__

  The white space between the top of the glyph and the visible beginning of the glyph.

- __tracking__

  Kerning between all glyphs in a line of text, not just the kerning pairs already defined by the font. You can increase or decrease interglyph spacing by adjusting the tracking setting. See [tracking setting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewueqkkijcueq2b); compare [kerning](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscjbfeesse).

- __tracking setting__

  A value that specifies the relative tightness or looseness of interglyph spacing.

- __trailing edge__

  The edge of a glyph that is encountered last when reading text of that glyph’s language. For glyphs of left-to-right text, the trailing edge is the right edge; for glyphs of right-to-left text, the trailing edge is the left edge.

- __triple__

  Three values that consist of an attribute tag, a value for that tag, and the size of the value. In ATSUI, triples are used to specify style, line, and layout attributes.

- __typestyle__

  See [text styles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewueqkkirfegskk).

- __typographic bounding rectangle__

  The smallest rectangle that encloses the full span of the glyphs from the ascent line to the descent line. See also [image bounding rectangle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewugsscincucscf).

- __typographic point__

  A unit of measurement describing the size of glyphs in a font. There are 72.27 typographic points per inch, as opposed to 72 points per inch in the Mac OS.

- __Unicode__

  A character encoding system designed to support the interchange, processing, and display of all the written texts of the diverse languages of the modern world.

- __Unicode decomposition__

  Splitting a composite glyph into its component parts, such as a base character and a combining mark.

- __variation axis__

  A range included in a font by the font designer that allows a font to produce different typestyles.

- __with-stream shift__

  A uniform shift parallel to the baseline of the positions of individual pairs or sets of glyphs in the style run. Compare [cross-stream shift](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobufvbuqmrrgewueqkkjfdeqrkf).

[Previous](Document%20Revision%20History.md)

