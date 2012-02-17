Name:		auteur
Version:	0.1a7
Release:	%mkrel 1
Summary:	Lightweight video editor powered by mplayer and mencoder
Group:		Video
License:	GPLv3
URL:		http://auteur-editor.info
Source0:	http://auteur-editor.info/releases/source_tarballs/%{name}-%{version}.tar.gz
BuildRequires:	python-devel
Requires:	PyQt4
Requires:	python-qt4-qscintilla
Requires:	mplayer
Requires:	mencoder

%description
The Auteur Non-Linear Editor is a project seeking to create a
professional-grade but user-friendly video editor.

%prep
%setup -q

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{python_sitelib}/*
%{_datadir}/%{name}

