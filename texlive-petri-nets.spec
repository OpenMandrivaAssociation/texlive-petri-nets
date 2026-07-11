%global tl_name petri-nets
%global tl_revision 39165

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A set TeX/LaTeX packages for drawing Petri nets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/petri-nets
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/petri-nets.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/petri-nets.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(petri-nets.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Petri-nets offers a set of TeX/LaTeX packages about Petri nets and
related models. Three packages are available: the first allows the user
to draw Petri-nets in PostScript documents; the second defines macros
related to PBC, M-nets and B(PN) models; and a third that combines the
other two.

