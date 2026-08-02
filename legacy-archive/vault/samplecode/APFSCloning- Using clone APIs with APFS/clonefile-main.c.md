---
title: 'APFSCloning: Using clone APIs with APFS'
apple_id: TP40017341
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/APFSCloning/Listings/clonefile_main_c.html
archived_at: '2026-07-18T02:59:40.034074Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [APFSCloning: Using clone APIs with APFS](APFSCloning-%20Using%20clone%20APIs%20with%20APFS.md)


[Next](README.md.md)[Previous](APFSCloning-%20Using%20clone%20APIs%20with%20APFS.md)

# clonefile/main.c

```c
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/errno.h>

#include <copyfile.h>      /* for copyfile(3)    */
#include <sys/clonefile.h> /* for clonefileat(2) */

int main(int argc, const char * argv[])
{
    int error;
    int was_cloned;
    copyfile_state_t s;

    if (argc != 3) {
        fprintf(stderr, "usage: %s src_file dst_file ...\n", argv[0]);
        exit(1);
    }

    /* Initailize state */
    s = copyfile_state_alloc();

    /* Copy the file (but clone if available)  */
    error = copyfile(argv[1], argv[2], s, COPYFILE_CLONE);
    if (error < 0) {
        perror("Error in copyfile()");
        exit(1);
    }

    /* Was the file cloned ? */
    if ((copyfile_state_get(s, COPYFILE_STATE_WAS_CLONED, &was_cloned) == 0) && was_cloned) {
        fprintf(stdout, "File was cloned\n");
    } else {
        fprintf(stdout, "File was copied and not cloned\n");
    }

    /* Release the state variable */
    copyfile_state_free(s);


    /* clone the file, this time using clonefileat(2) instead of copyfile(3) */
    (void)unlink(argv[2]);

    error = clonefileat(AT_FDCWD, argv[1], AT_FDCWD, argv[2], 0);
    if (error < 0) {
        perror("Error in clonefileat()");
        exit(1);
    }

    return (0);
}
```

[Next](README.md.md)[Previous](APFSCloning-%20Using%20clone%20APIs%20with%20APFS.md)

