%global tl_name shapepar
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	A macro to typeset paragraphs in specific shapes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/shapepar
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shapepar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shapepar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
\shapepar is a macro to typeset paragraphs in a specific shape. The size
is adjusted automatically so that the entire shape is filled with text.
There may not be displayed maths or '\vadjust' material (no \vspace) in
the argument of \shapepar. The macros work for both LaTeX and plain TeX.
For LaTeX, specify \usepackage{shapepar}; for Plain, \input
shapepar.sty. \shapepar works in terms of user-defined shapes, though
the package does provide some predefined shapes: so you can form any
paragraph into the form of a heart by putting \heartpar{sometext...}
inside your document. The tedium of creating these polygon definitions
may be alleviated by using the shapepatch extension to transfig which
will convert xfig output to \shapepar polygon form.

