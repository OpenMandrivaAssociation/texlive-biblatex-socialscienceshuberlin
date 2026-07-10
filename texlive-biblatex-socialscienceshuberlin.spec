%global tl_name biblatex-socialscienceshuberlin
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.1
Release:	%{tl_revision}.1
Summary:	BibLaTeX-style for the social sciences at HU Berlin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-socialscienceshuberlin
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-socialscienceshuberlin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-socialscienceshuberlin.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a BibLaTeX style for the social sciences at the Humboldt-
Universitat zu Berlin.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-socialscienceshuberlin
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-socialscienceshuberlin
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-socialscienceshuberlin/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-socialscienceshuberlin/socialscienceshuberlin-examples.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-socialscienceshuberlin/socialscienceshuberlin.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-socialscienceshuberlin/socialscienceshuberlin.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-socialscienceshuberlin/german-socialscienceshuberlin.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-socialscienceshuberlin/socialscienceshuberlin.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-socialscienceshuberlin/socialscienceshuberlin.cbx
