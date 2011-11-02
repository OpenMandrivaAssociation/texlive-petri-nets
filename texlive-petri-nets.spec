Name:		texlive-petri-nets
Version:	20070112
Release:	1
Summary:	A set TeX/LaTeX packages for drawing Petri nets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/petri-nets
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/petri-nets.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/petri-nets.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Petri-nets is a set of TeX/LaTeX packages about Petri nets and
related models. Three packages are available: - the first
allows the user to draw Petri-nets in PostScript documents; -
the second defines macros related to PBC, M-nets and B(PN)
models; and - the last gathers together the previous two.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/petri-nets/pndraw.sty
%{_texmfdistdir}/tex/generic/petri-nets/pndraw.tex
%{_texmfdistdir}/tex/generic/petri-nets/pnets.sty
%{_texmfdistdir}/tex/generic/petri-nets/pnets.tex
%{_texmfdistdir}/tex/generic/petri-nets/pntext.sty
%{_texmfdistdir}/tex/generic/petri-nets/pntext.tex
%{_texmfdistdir}/tex/generic/petri-nets/pnversion.tex
%doc %{_texmfdistdir}/doc/generic/petri-nets/COPYING
%doc %{_texmfdistdir}/doc/generic/petri-nets/ChangeLog
%doc %{_texmfdistdir}/doc/generic/petri-nets/README
%doc %{_texmfdistdir}/doc/generic/petri-nets/pn2pdf
%doc %{_texmfdistdir}/doc/generic/petri-nets/pndoc.pdf
%doc %{_texmfdistdir}/doc/generic/petri-nets/pndoc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}