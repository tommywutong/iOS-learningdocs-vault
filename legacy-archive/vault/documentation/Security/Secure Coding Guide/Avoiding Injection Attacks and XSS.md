---
title: Secure Coding Guide
apple_id: TP40002415
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/OtherHardeningTechniques/OtherHardeningTechniques.html
archived_at: '2026-07-18T02:06:26.950081Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Secure Coding Guide](Introduction%20to%20Secure%20Coding%20Guide.md)


[Next](Security%20Development%20Checklists.md)[Previous](Designing%20Secure%20Helpers%20and%20Daemons.md)

# Avoiding Injection Attacks and XSS

Injection attacks and cross-site scripting (XSS) are two types of vulnerabilities often associated with web development. However, similar problems can occur in any type of application. By becoming familiar with these types of attacks and understanding the antipatterns that they represent, you can avoid them in your software.

There are two types of data in the world: unstructured data and structured data. The type you choose can have a significant impact on what you must do to make your software secure.

Unstructured data is rare. It mainly includes plain text files when they are used solely as a means of displaying text. More often than not, what appears to be unstructured data is actually weakly structured data.

With structured data, different parts of the data have different meaning. Whenever a single piece of data contains two or more different types of data in this way, the potential for injection attacks exists. The potential risks vary depending on how you mix the data—specifically, whether it is _strictly structured_ or _weakly structured_.

Strictly structured data has a fixed format that defines where each piece of information should be stored. A simple data format for a store’s inventory might, for example, specify that there should be 4 bytes containing a record number followed by 100 bytes of human-readable description. Strictly structured data is fairly straightforward to work with. Although the interpretation of each byte depends on its location within the data, as long as you avoid overflowing any fixed-size buffers and do appropriate checks to ensure the values make sense, the security risks are usually relatively low.

Weakly structured data, however, is somewhat more problematic from a security perspective. Weakly structured data is a hybrid scheme in which portions of the data have variable length. Weakly structured data can be further divided into one of two categories: _explicitly sized_ data and _implicitly sized_ data.

Explicitly sized data provides a length value at the start of any variable-length data. For the most part, such data is straightforward to interpret, but care must be taken to ensure that the length values are reasonable. They should not, for example, extend past the end of the file.

Implicitly sized data is more difficult to interpret. It uses special delimiter characters within the data itself to describe how the data should be interpreted. For example, it might use commas to separate fields, or quotation marks to separate data from the commands that operate on that data. For example, SQL and shell command mix the command words themselves with the data that the command operates on. HTML files mix tags with text. And so on.

Because unstructured, strictly structured, and weakly structured data with explicit lengths are less likely to pose security risks, the remainder of this section focuses on weakly structured data with implicit lengths.

As mentioned previously, whenever you mix two types of data—control statements and actual data separated by delimiters, for example—you run the risk of misbehavior. These risks must be considered both when reading data and when constructing data for later use.

The easiest way to demonstrate the problem is by example. Consider the following snippet of JSON data:

```json
{
    "mydictionary" :
    {
        "foo" : "Computer jargon",
        "bar" : "More computer jargon"
    }
}
```

This structure describes a nested set of key-value pairs. The keys—`mydictionary`, `foo`, and `bar`—are of variable length, as are their values (a dictionary, plus the strings `Computer jargon` and `More computer jargon`. Their length is determined by a _parser_—a piece of software that reads and analyzes a complex piece of data, splitting it into its constituent parts. When parsing JSON data, the parser looks for a double quotation mark that marks the beginning and end of each string.

Now suppose that your software is an online dictionary that allows users to add words, checking them to make sure they are not impolite words before adding them. What happens if the user maliciously enters something like the following?

```
Term: baz
Definition: Still more computer jargon", "naughtyword": "A word you should not say
```

A naive piece of software might insert the definition into the JSON file by wrapping both the term and definition (as is) in quotation marks. The resulting JSON file would look like this:

```json
{
    "mydictionary" :
    {
        "foo" : "Computer jargon",
        "bar" : "More computer jargon",
        "baz" : "Still more computer jargon", "naughtyword": "A word you should not say"
    }
}
```

Because whitespace is not significant in JSON, the result is that _two_ terms have now been added to the dictionary, and the second term was never checked for politeness by your software.

Instead, the software should have performed _quoting_ on the data—scanning the input for characters that have special meaning in the context of the enclosing content and modifying or otherwise marking them so that they are not interpreted as special characters. For example, you can protect quotation marks in JSON by preceding them with a backslash (`\`), as shown here:

```json
{
    "mydictionary" :
    {
        "foo" : "Computer jargon",
        "bar" : "More computer jargon",
        "baz" : "Still more computer jargon\", \"naughtyword\": \"A word you should not say"
    }
}
```

Now, when the parser reads the JSON, it correctly reads the definition of baz as `Still more computer jargon.", "naughtyword": "A word you should not say`. Thus, the naughty word is not defined, because it is just part of the definition of baz. Of course, this still leaves the question of whether you should have checked for inappropriate words in the definitions, but that’s a separate question.

The most common type of injection attack is SQL injection, a technique that takes advantage of the syntax of SQL to inject arbitrary commands. A SQL statement looks something like this:

```
INSERT INTO users (name, description) VALUES ("John Doe", "A really hoopy frood.");
```

This example contains a mixture of instructions (the `INSERT` statement itself) and data (the strings to be inserted).

Naive software might construct a query manually by simple string concatenation. Such an approach is very dangerous, particularly if the data comes from an untrusted source, because if the user name or description contains a double quotation mark, that untrusted source can then provide command data instead of value data.

To compound the problem, the SQL language provides a comment operator, `--`, which causes the SQL server to ignore the rest of the line. For example, if a user enters the following text as his or her user name:

```
joe", "somebody"); DROP TABLE users; --
```

the resulting command would looks like this:

```
INSERT INTO users (name, description) VALUES ("joe", "somebody"); DROP TABLE users; --", "A really hoopy frood.");
```

and the database would insert the user, but would then dutifully delete all user accounts and the table that holds them, rendering the service nonfunctional.

A slightly less naive program might check for double quotation marks and refuse to allow you to use them in your user name or description. As a rule, this is undesirable for several reasons:

- This approach may not be compatible with UTF-8. UTF-8 characters frequently contain the same numeric values as quotation marks, which means that (for example) a capital G with a cedilla might be incorrectly stored in your database, depending on how your SQL server handles UTF-8 (or doesn’t).
- If you change your query slightly to use single quotes, your solution breaks.
- If the user puts a backslash before the quotation mark, your solution breaks (unless you also quote those) because the two backslashes are then treated as a literal character.
- If you check for illegal characters in JavaScript but do not perform similar checks on the server side, a malicious user can get around the checks and inject code anyway.
- If you check for illegal characters in JavaScript, because the user cannot easily see whether you have similar checks on the server side, your users will worry about your site’s security.
- One of your users might really want his or her user name to be `"; DROP TABLE users; --` or perhaps something slightly less extreme.

Instead, the correct solution is to either use your SQL client library’s built-in functions for quoting strings or, where possible, to use parameterized SQL queries in which you substitute placeholders for the strings themselves. For example, a parameterized SQL query might look like this:

```
INSERT INTO users (name, description) VALUES (?, ?);
```

You would then provide the name and description values out-of-band in an array. Depending on how your particular database implementation handles these sorts of queries, the statement might still get converted back into the same mixed-data query, but given the number of people who use most major databases, mistakes in any conversion routines provided by the database itself are likely to be caught and fixed quickly.

For more information about avoiding SQL injection attacks on applications that use Core Data in complex ways, read [Creating Predicates](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pCreating.html#//apple_ref/doc/uid/TP40001793) in _[Predicate Programming Guide](../../Cocoa/Predicate%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoobz)_.

In the C programming language, there are a number of acceptable ways to execute an external command, using [exec](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/exec.3.html#//apple_ref/doc/man/3/exec), [posix_spawn](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/posix_spawn.2.html#//apple_ref/doc/man/2/posix_spawn), [NSTask](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/cl/NSTask), and related functions and classes. There are also many wrong ways to use these and other functions. This section provides some tips on how to avoid security holes when running external commands.

- __Don’t use system.__ The [system](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/system.3.html#//apple_ref/doc/man/3/system) function runs an external shell process and passes a command string directly to that shell. This means that you must properly quote any arguments that you pass to the commands. The `system` function is particularly problematic if those arguments come from potentially untrusted sources. For this reason, you should avoid using the `system` function except with hard-coded commands.
- __Don’t use popen.__ The [popen](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/popen.3.html#//apple_ref/doc/man/3/popen) has the same security risks as `system`. Instead of using `popen`, either use the `NSTask` class or construct the pipe and execute the command yourself.

  The [NSTask](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/cl/NSTask) class makes it easy to communicate with the standard input, output, and error descriptors of a child process. You can learn more by reading _[NSTask Class Reference](https://developer.apple.com/documentation/foundation/nstask)_.

  At the POSIX level you can achieve the same thing with the [pipe](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/pipe.2.html#//apple_ref/doc/man/2/pipe) system call, as follows:

  1. Use the [pipe](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/pipe.2.html#//apple_ref/doc/man/2/pipe) system call to create one or more pairs of connected pipes.
  2. Use the `fork` system call to create a child process.
  3. In the child process, use the [dup2](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/dup2.2.html#//apple_ref/doc/man/2/dup2) system call to replace one or more of the standard input, standard output, and standard error file descriptors with the pipe endpoint of your choice.
  4. In the child process, use [exec](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/exec.3.html#//apple_ref/doc/man/3/exec), [posix_spawn](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/posix_spawn.2.html#//apple_ref/doc/man/2/posix_spawn), or related functions to start the desired tool.
  5. In the parent process, read from or write to the opposite end of each pipe.

  For example:

```
int pipes[2];
if (pipe(pipes) < -1) {
    ... // Handle the error
}

int pid = fork();
if (pid == -1) {
    ... // Handle the error
} else if (!pid) {
    // In the child process:

    dup2(pipe[1], STDOUT_FILENO); // or STDIN_FILENO or STDERR_FILENO
    close(pipe[0]);

    exec(...) or posix_spawn(...) // Run the external tool.

} else {
    // In the parent process:

    close(pipe[1]);
    read(pipe[0], ...);

    waitpid(pid, ...); // Wait for the child process to go away.
}
```

  For details, see the manual pages for [pipe](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/pipe.2.html#//apple_ref/doc/man/2/pipe), `fork`, [dup2](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/dup2.2.html#//apple_ref/doc/man/2/dup2), [exec](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/exec.3.html#//apple_ref/doc/man/3/exec), [posix_spawn](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/posix_spawn.2.html#//apple_ref/doc/man/2/posix_spawn), and [waitpid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/waitpid.2.html#//apple_ref/doc/man/2/waitpid).
- __Avoid shell scripts where possible.__ Whether you are using `NSTask` or any of the functions above, avoid using shell scripts to execute commands, because shell quoting is easy to get wrong. Instead, execute the commands individually.
- __Audit any shell scripts.__ If your software runs shell scripts and passes potentially untrusted data to them, your software could be affected by any quoting bugs in those scripts. You should carefully audit these scripts for quoting errors that might lead to security holes.

  For more information, read [Quoting Special Characters](../../Shell%20Scripting%20Primer/Flow%20Control%2C%20Expansion%2C%20and%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnbnknlteoa) and [Shell Script Security](https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/ShellScriptSecurity/ShellScriptSecurity.html#//apple_ref/doc/uid/TP40004268-CH8) in _[Shell Scripting Primer](../../Shell%20Scripting%20Primer/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denry)_.

The rules for quoting a URL are complex and are beyond the scope of this document. macOS and iOS provide routines to help you, but you must be certain to use the _correct_ routine for what you are trying to do.

To learn more, read [Converting Strings to URL Encoding](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/WorkingWithHTTPAndHTTPSRequests/WorkingWithHTTPAndHTTPSRequests.html#//apple_ref/doc/uid/TP40010220-CH8-SW7) in _[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_.

The safest way to work with HTML and XML is to use a library that provides objects for each node, such as the [NSXMLParser](https://developer.apple.com/documentation/foundation/xmlparser) class or the `libxml2` API. However, if you must construct HTML or XML manually, there are five special characters that must be quoted explicitly when converting text to HTML or XML:

- Less than (`<`)—Replace with `<` everywhere
- Greater than (`>`)—Replace with `>` everywhere
- Ampersand (`&`)—Replace with `&` everywhere
- Double quote (`"`)—Replace with `"` inside attribute values
- Single quote (`"`)—Replace with `&apos;` inside attribute values

To learn more about the security holes that can result from failure to quote HTML content properly, read [Avoiding Cross-Site Scripting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmznknlto).

Another significant risk associated with web development is _cross-site scripting_. Cross-site scripting refers to injecting code into a website that causes it to behave differently than it otherwise would. An attacker might, for example, inject a key logger that displays a fake login dialog and sends the passwords back to the attacker.

There are many types of cross-site scripting vulnerabilities:

- If a website displays content provided in a URL query string without proper sanitization, an attacker can create a hyperlink that executes arbitrary JavaScript code. When the victim follows that link, the attacker-provided script runs in the victim’s browser session.
- Websites that allow users to share HTML-based content with one another can inadvertently serve malicious JavaScript code provided by users, whether in a standalone script tag or hidden in various HTML attributes and CSS properties. When another user visits that page, the malicious JavaScript code runs in the victim’s browser session.
- Scripts that use `eval` on strings that contain user-provided data can be made to execute arbitrary code if they do not properly sanitize that user-provided data.

And so on. The details of cross-site scripting are beyond the scope of this document. To learn more about cross-site scripting and about how to avoid it, read [XSS Prevention Cheat Sheet](https://www.owasp.org/index.php/XSS_%28Cross_Site_Scripting%29_Prevention_Cheat_Sheet). From there, you can find links to a number of other articles on web security. You can also find a number of third-party books on cross-site scripting.

[Next](Security%20Development%20Checklists.md)[Previous](Designing%20Secure%20Helpers%20and%20Daemons.md)

