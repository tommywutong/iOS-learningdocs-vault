---
title: 'Logging: Using the os_log APIs'
apple_id: TP40017510
resource_type: Sample Code
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Logging/Listings/find_largest_file_find_largest_file_main_c.html
archived_at: '2026-07-18T03:13:47.990094Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Logging: Using the os_log APIs](Logging-%20Using%20the%20oslog%20APIs.md)


[Next](find-largest-file-ReadMe.md.md)[Previous](Paper%20Company%20%28Swift%29-ReadMe.md.md)

# find-largest-file/find-largest-file/main.c

```c
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Basic demonstration of how to use select Logging APIs.
 */

#include <dirent.h>
#include <errno.h>
#include <sys/stat.h>
#include <os/log.h>


size_t find_largest_file(const char *dirpath, char largest_file_path[PATH_MAX]) {
    size_t cur_max_filesize = 0; // The size of the largest file found within the current directory.

    if (dirpath == NULL) { // Safety first.
        return 0;
    }

    DIR *d = opendir(dirpath);
    if (d == NULL) {
        /*
            Here we use `os_log_info` because while we did encounter an error while
        trying to access a directory, it's nothing out of the ordinary.
        `os_log_error` captures the log messages preceding the error and saves
        them to disk, which is not an insignificant amount of work. See
        `os_log_info` below for more information on this system.
        */
        os_log_info(OS_LOG_DEFAULT, "Unable to access directory %s: %{errno}d", dirpath, errno);
        return 0;
    }

    // Successfully opened directory.

    /*
        `os_log_info` is used here because this is information that could be useful
    when troubleshooting a problem, just to get a sense of what the program
    was doing before it ran into an issue. With the default configuration,
    messages logged with `os_log_info` are saved in memory only, not to disk.
    If no error occurs, these messages will eventually be discarded. But if
    an error occurs, the most recent of these messages will be saved to disk
    to help troubleshoot the issue.
    */
    os_log_info(OS_LOG_DEFAULT, "Entering directory %s", dirpath);
    int cur_dir_fd = dirfd(d);
    struct dirent *dir;
    // Do all files first.
    while ((dir = readdir(d)) != NULL) {
        if (dir->d_type != DT_REG) {
            // Files only.
            continue;
        }

        // Stat the file.
        struct stat file_stat;
        if (fstatat(cur_dir_fd, dir->d_name, &file_stat, AT_SYMLINK_NOFOLLOW) == -1) {
            /*
                There was an error opening the current file, so we log the file
            that we can't open, and capture what we were doing before this.
            These strings are logged dynamically (i.e., they're not known at
            compile-time), so they are (by default) private information and
            will be redacted. The `{public}` specifier is used to override this.
            */
            os_log_error(OS_LOG_DEFAULT, "Cannot stat file %s/%s: %{public,errno}d", dirpath, dir->d_name, errno);
            continue;
        }
        /*
            This debug message is used to provide copious amounts of
        information. The idea is that the debug level of logging is only
        enabled when trying to troubleshoot a specific bug during
        development. These messages are in memory only (again, by
        default), and are saved only when a call to `os_log_error` or
        `os_log_fault` is made.
        */
        os_log_debug(OS_LOG_DEFAULT, "Processing file %s/%s", dirpath, dir->d_name);

        // Get the file's size.
        if (file_stat.st_size > cur_max_filesize) {
            cur_max_filesize = file_stat.st_size;
            strncpy(largest_file_path, dirpath, PATH_MAX);
            strncat(largest_file_path, "/", 1);
            strncat(largest_file_path, dir->d_name, dir->d_namlen);
            // Spit out a quick progress update for anybody that may be watching our logs live.

            /*
                For privacy reasons, dynamic strings and most dynamic objects are
            considered to be private, and are redacted in log messages
            automatically. Static strings and scalar values are public. Format
            specifiers can be used to change the default privacy of a given
            element, as shown here.
            NOTE: This string is marked as public in order to demonstrate how
            to properly use the format specifiers. The name of a file on a
            user's system should be private.
            */
            os_log_info(OS_LOG_DEFAULT, "%{public}s is the new largest file in the current directory with size %{private}zu bytes", largest_file_path, cur_max_filesize);
        }
    }

    // Now recurse on all the directories in the current directory.
    rewinddir(d);
    while ((dir = readdir(d)) != NULL) {
        if (dir->d_type != DT_DIR) {
            // Directories only.
            continue;
        }
        if (strcmp(dir->d_name, ".") == 0 || strcmp(dir->d_name, "..") == 0) {
            // Skip . and ..
            continue;
        }

        // Set up the path to each subdirectory.
        char cur_path[PATH_MAX] = { 0 };
        strncpy(cur_path, dirpath, PATH_MAX);
        strncat(cur_path, "/", 1);
        strncat(cur_path, dir->d_name, dir->d_namlen);

        // Recurse on each subdirectory.
        size_t largest_in_dir = find_largest_file(cur_path, largest_file_path);
        if (largest_in_dir > cur_max_filesize) {
            cur_max_filesize = largest_in_dir;
        }
    }

    // We're done reading the directory's contents, so close and return.
    closedir(d);
    return cur_max_filesize;
}


int main(int argc, const char * argv[]) {
    char largest_path[PATH_MAX] = { 0 };
    size_t largest_file_size;
    char search_root_path[PATH_MAX] = "/";

    // If an argument is present, use it as the root path to search in.
    if (argc == 2) {
        realpath(argv[1], search_root_path);
    }

    /*
        `os_log` is used for the most relevant information. This is saved to disk
    by default, and is used for important events in the application, such as
    beginning a task. See also the Paper Company sample code for more detail on
    logging by activity in your application.
    */
    os_log(OS_LOG_DEFAULT, "Searching for the largest file in %s", search_root_path);
    largest_file_size = find_largest_file(search_root_path, largest_path);
    os_log(OS_LOG_DEFAULT, "The largest file is %s with a size of %zu bytes.", largest_path, largest_file_size);
    printf("The largest file is %s with a size of %zu bytes.\n", largest_path, largest_file_size);

    return 0;
}
```

[Next](find-largest-file-ReadMe.md.md)[Previous](Paper%20Company%20%28Swift%29-ReadMe.md.md)

