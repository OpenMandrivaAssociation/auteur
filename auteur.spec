Summary:	Lightweight video editor powered by mplayer and mencoder
Name:		auteur
Version:	0.1a7
Release:	3
License:	GPLv3+
Group:		Video
Url:		http://auteur-editor.info
Source0:	http://auteur-editor.info/releases/source_tarballs/%{name}-%{version}.tar.gz
Patch0:		auteur-0.1a7-desktop.patch
BuildRequires:	pkgconfig(python)
Requires:	mencoder
Requires:	mplayer
Requires:	PyQt4
Requires:	python-qt4-qscintilla
BuildArch:	noarch

%description
The Auteur Non-Linear Editor is a project seeking to create a
professional-grade but user-friendly video editor.

%files
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{python_sitelib}/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

mv %{buildroot}%{_datadir}/applications/Auteur.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

