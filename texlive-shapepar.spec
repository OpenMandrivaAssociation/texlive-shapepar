# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/shapepar
# catalog-date 2009-10-10 00:35:28 +0200
# catalog-license other-free
# catalog-version 2.1
Name:		texlive-shapepar
Version:	2.1
Release:	2
Summary:	A macro to typeset paragraphs in specific shapes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/shapepar
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shapepar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shapepar.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
\shapepar is a macro to typeset paragraphs in a specific shape.
The size is adjusted automatically so that the entire shape is
filled with text. There may not be displayed maths or
'\vadjust' material (no \vspace) in the argument of \shapepar.
The macros work for both LaTeX and plain TeX. For LaTeX,
specify \usepackage{shapepar}; for Plain, \input shapepar.sty.
\shapepar works in terms of user-defined shapes, though the
package does provide some predefined shapes: so you can form
any paragraph into the form of a heart by putting
\heartpar{sometext...} inside your document. The tedium of
creating these polygon definitions may be alleviated by using
the shapepatch extension to transfig which will convert xfig
output to \shapepar polygon form.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/shapepar/shapepar.sty
%doc %{_texmfdistdir}/doc/generic/shapepar/Canflagshape.def
%doc %{_texmfdistdir}/doc/generic/shapepar/README.shapepar
%doc %{_texmfdistdir}/doc/generic/shapepar/TeXshape.def
%doc %{_texmfdistdir}/doc/generic/shapepar/candleshape.def
%doc %{_texmfdistdir}/doc/generic/shapepar/dropshape.def
%doc %{_texmfdistdir}/doc/generic/shapepar/proshap.py
%doc %{_texmfdistdir}/doc/generic/shapepar/shapepar.ltx
%doc %{_texmfdistdir}/doc/generic/shapepar/shapepar.pdf
%doc %{_texmfdistdir}/doc/generic/shapepar/triangleshapes.def

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-2
+ Revision: 755979
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 719523
- texlive-shapepar
- texlive-shapepar
- texlive-shapepar
- texlive-shapepar

