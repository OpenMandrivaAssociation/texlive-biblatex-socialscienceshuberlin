Name:		texlive-biblatex-socialscienceshuberlin
Version:	47839
Release:	1
Summary:	BibLaTeX-style for the social sciences at HU Berlin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-socialscienceshuberlin
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-socialscienceshuberlin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-socialscienceshuberlin.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a BibLaTeX style for the social sciences at the
Humboldt-Universitat zu Berlin.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-socialscienceshuberlin
%doc %{_texmfdistdir}/doc/latex/biblatex-socialscienceshuberlin

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
