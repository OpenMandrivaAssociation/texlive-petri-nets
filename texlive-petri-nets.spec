Name:		texlive-petri-nets
Version:	20180303
Release:	2
Summary:	A set TeX/LaTeX packages for drawing Petri nets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/petri-nets
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/petri-nets.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/petri-nets.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Petri-nets is a set of TeX/LaTeX packages about Petri nets and
related models. Three packages are available: - the first
allows the user to draw Petri-nets in PostScript documents; -
the second defines macros related to PBC, M-nets and B(PN)
models; and - the last gathers together the previous two.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/petri-nets
%{_texmfdistdir}/scripts/petri-nets
%doc %{_texmfdistdir}/doc/generic/petri-nets

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar texmf-dist/tex texmf-dist/doc texmf-dist/scripts %{buildroot}%{_texmfdistdir}
