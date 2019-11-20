# Nipype 1 legacy workflows

This package includes the workflows built up over nearly a decade of development of
[Nipype](https://nipy.org/nipype/).

These workflows were contributed by various users and developers, and are more-or-less tied to the
specific contexts, in terms of available tools and interfaces, as well as consensus best practices,
at the time each was developed. It is laborious to identify which have been updated to accommodate
changes in underlying software or changing ideas of best practice, and which serve primarily as a
public record of a particular effort.

The Nipype developers have decided to initiate the [niflows](https://github.com/niflows) project,
which will allow new workflows, or collections of workflows, to be separately packaged and made
available under a common interface and in a common namespace. This will permit each niflow
repository and associated package to describe its history in a natural way, and the level of
maintenance of a package will not be obscured by the development process of nipype itself.

This package serves as an example niflow. In general, it exists as a historical record, and updates
to this package will be for the sake of further developing niflows. If a bug is found in one of
these workflows that was not introduced by moving the workflows out of nipype, then the preferred
response is to publish a new niflow.
