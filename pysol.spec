Summary:	PySol - a solitaire game collection
Summary(pl.UTF-8):	PySol - kolekcja pasjansów
Name:		pysol
Version:	4.82
Release:	7
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	31a3ed96c6feb54717c6bce9ddd82b24
Source1:	%{name}-cardsets-4.40.tar.bz2
# Source1-md5:	cdf3749865b2f3b9d60950a9fb87185a
Source2:	%{name}-music-4.40.tar.bz2
# Source2-md5:	08717045ef86825a1e59d5f66c3bf720
#Source3Download: http://www.pysol.org/
Source3:	http://www.pysol.org/download/pysol/%{name}-%{version}-src.tar.bz2
# Source3-md5:	be0fd45c016fe2dcacb03fb29871aff4
Source4:	%{name}.desktop
Source5:	%{name}.png
Patch0:		%{name}-python23.patch
URL:		http://www.pysol.org/
BuildRequires:	python >= 1:2.3
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	rpm-pythonprov
Requires:	pysol-sound-server >= 3.00
Requires:	python >= 1:2.3
%pyrequires_eq	python-tkinter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dotless_pyver	%(echo %{py_ver}|tr -d .)

%description
- currently supports more than 200 distinct solitaire games,
- based upon an extensible solitaire engine,
- lots of classic games like Forty Thieves, FreeCell, Klondike and
  Spider,
- special games like Ganjifa, Hanafuda, Poker and Tarock type games,
- very nice look and feel,
- multiple cardsets and backgrounds,
- background table tiles,
- unlimited undo & redo,
- persistent bookmarks,
- load & save games,
- player statistics,
- hint system,
- demo games,
- support for user written plug-ins,
- sound samples and background music,
- integrated HTML help browser,
- lots of documentation,
- written in 100%% pure Python.

%description -l pl.UTF-8
- zawiera ponad 200 różnych typów pasjansów,
- oparty na rozbudowywalnym silniku,
- mnóstwo klasycznych gier, takich jak Forty Thieves, FreeCell,
  Klondike i Spider,
- specjalne gry, jak Ganjifa, Hanafuda, Poker i Tarock,
- ładny wygląd,
- wiele zestawów kart i teł,
- kafelkowane tło,
- nieskończone undo i redo,
- trwałe zakładki,
- ładowanie i zapisywanie gier,
- statystyki gracza,
- system podpowiedzi,
- demonstracje,
- wsparcie dla wtyczek użytkownika,
- dźwięki i muzyka w tle,
- zintegrowana przeglądarka pomocy w HTML-u,
- mnóstwo dokumentacji,
- napisane w 100%% w Pythonie.

%package cardsets-classic_look
Summary:	Additional cardsets for PySol
Summary(pl.UTF-8):	Dodatkowe zestawy kart dla PySola
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description cardsets-classic_look
Additional cardsets (Classic look) for PySol.

%description cardsets-classic_look -l pl.UTF-8
Dodatkowe zestawy kart (Klasyczny wygląd) dla PySola.

%package cardsets-collectors-1-D
Summary:	Additional cardsets for PySol
Summary(pl.UTF-8):	Dodatkowe zestawy kart dla PySola
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description cardsets-collectors-1-D
Additional cardsets (Collectors 1-D) for PySol.

%description cardsets-collectors-1-D -l pl.UTF-8
Dodatkowe zestawy kart (Kolekcjonerskie 1-D) dla PySola.

%package cardsets-collectors-F-J
Summary:	Additional cardsets for PySol
Summary(pl.UTF-8):	Dodatkowe zestawy kart dla PySola
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description cardsets-collectors-F-J
Additional cardsets (Collectors F-J) for PySol.

%description cardsets-collectors-F-J -l pl.UTF-8
Dodatkowe zestawy kart (Kolekcjonerskie F-J) dla PySola.

%package cardsets-collectors-L-N
Summary:	Additional cardsets for PySol
Summary(pl.UTF-8):	Dodatkowe zestawy kart dla PySola
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-collectors-L-N
Additional cardsets (Collectors L-N) for PySol.

%description cardsets-collectors-L-N -l pl.UTF-8
Dodatkowe zestawy kart (Kolekcjonerskie L-N) dla PySola.

%package cardsets-collectors-P-W
Summary:	Additional cardsets for PySol
Summary(pl.UTF-8):	Dodatkowe zestawy kart dla PySola
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-collectors-P-W
Additional cardsets (Collectors P-W) for PySol.

%description cardsets-collectors-P-W -l pl.UTF-8
Dodatkowe zestawy kart (Kolekcjonerskie P-W) dla PySola.

%package cardsets-fantasy
Summary:	Additional cardsets for PySol
Summary(pl.UTF-8):	Dodatkowe zestawy kart dla PySola
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-fantasy
Additional cardsets (Fantasy) for PySol.

%description cardsets-fantasy -l pl.UTF-8
Dodatkowe zestawy kart (Fantastyczne) dla PySola.

%package cardsets-os
Summary:	Additional cardsets for PySol
Summary(pl.UTF-8):	Dodatkowe zestawy kart dla PySola
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-os
Additional cardsets (Operating Systems) for PySol.

%description cardsets-os -l pl.UTF-8
Dodatkowe zestawy kart (Systemy operacyjne) dla PySola.

%package cardsets-round
Summary:	Additional cardsets for PySol
Summary(pl.UTF-8):	Dodatkowe zestawy kart dla PySola
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-round
Additional cardsets (Round cardsets) for PySol.

%description cardsets-round -l pl.UTF-8
Dodatkowe zestawy kart (Krągłe karty) dla PySola.

%package cardsets-uncategorized
Summary:	Additional cardsets for PySol
Summary(pl.UTF-8):	Dodatkowe zestawy kart dla PySola
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-uncategorized
Additional cardsets (Uncategorized) for PySol.

%description cardsets-uncategorized -l pl.UTF-8
Dodatkowe zestawy kart (Nieskatalogowane) dla PySola.

%package sounds
Summary:	Sounds for PySol
Summary(pl.UTF-8):	Dźwięki dla PySola
Group:		X11/Applications/Games
Requires:	%{name}
Requires:	%{name}-sound-server >= 3.00

%description sounds
Sounds for PySol.

%description sounds -l pl.UTF-8
Dźwięki dla PySola.

%package music
Summary:	Background music for PySol
Summary(pl.UTF-8):	Muzyka dla PySola
Group:		X11/Applications/Games
Requires:	%{name}
Requires:	%{name}-sound-server >= 3.00

%description music
Background music for PySol.

%description music -l pl.UTF-8
Muzyka dla PySola.

%prep
%setup -q -a 1 -a 2 -a 3

%{__rm} -r data/cardset-2000 data/cardset-colossus data/cardset-hard-a-port \
	data/cardset-hexadeck data/cardset-kintengu data/cardset-tuxedo \
	data/cardset-vienna-2k data/cardset-oxymoron
%{__rm} data/pysol_*.pyc
for i in pysol-cardsets-4.40/data/*; do
	mv $i data/;
done
for i in pysol-music-4.40/data/music/*; do
	mv $i data/music/;
done
mv %{name}-%{version}/src .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_bindir},%{_datadir}} \
	$RPM_BUILD_ROOT{%{_mandir}/man6,%{_pixmapsdir},%{py_sitedir}/pysol}

sed s\|@pkgdatadir@\|%{_datadir}/pysol\| pysol > $RPM_BUILD_ROOT%{_bindir}/pysol
cp -a data $RPM_BUILD_ROOT%{_datadir}/pysol

install pysol.6 $RPM_BUILD_ROOT%{_mandir}/man6/pysol.6
install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}

cp -R src/* $RPM_BUILD_ROOT%{py_sitedir}/pysol
ln -sf %{py_sitedir}/pysol/pysol.pyc $RPM_BUILD_ROOT%{_datadir}/pysol/pysol_%{dotless_pyver}.pyc
%py_comp $RPM_BUILD_ROOT%{py_sitedir}/pysol
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/pysol
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/pysol
%dir %{py_sitedir}/pysol
%{py_sitedir}/pysol/*.py[co]
%dir %{py_sitedir}/pysol/games
%{py_sitedir}/pysol/games/*.py[co]
%dir %{py_sitedir}/pysol/games/contrib
%{py_sitedir}/pysol/games/contrib/*.py[co]
%dir %{py_sitedir}/pysol/games/special
%{py_sitedir}/pysol/games/special/*.py[co]
%dir %{py_sitedir}/pysol/tk
%{py_sitedir}/pysol/tk/*.py[co]
%dir %{_datadir}/pysol
%{_datadir}/pysol/html
%{_datadir}/pysol/images
%{_datadir}/pysol/plugins
%{_datadir}/pysol/tiles
%{_datadir}/pysol/toolbar
%{_datadir}/pysol/pysol*
%{_datadir}/pysol/cardset-hard-a-port
%{_datadir}/pysol/cardset-hexadeck
%{_datadir}/pysol/cardset-kintengu*
%{_datadir}/pysol/cardset-vienna-2k
%{_mandir}/man6/pysol.6*
%{_pixmapsdir}/pysol.png
%{_desktopdir}/pysol.desktop

%files cardsets-classic_look
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-2000
%{_datadir}/pysol/cardset-briscola
%{_datadir}/pysol/cardset-xskat*

%files cardsets-collectors-1-D
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-1*
%{_datadir}/pysol/cardset-culemann*
%{_datadir}/pysol/cardset-denizens
%{_datadir}/pysol/cardset-dondorf*

%files cardsets-collectors-F-J
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-fantasy
%{_datadir}/pysol/cardset-gortz*
%{_datadir}/pysol/cardset-hamburg*
%{_datadir}/pysol/cardset-hegewald*
%{_datadir}/pysol/cardset-houbigant
%{_datadir}/pysol/cardset-hungarian*
%{_datadir}/pysol/cardset-joan-darc

%files cardsets-collectors-L-N
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-revolution*
%{_datadir}/pysol/cardset-liege
%{_datadir}/pysol/cardset-little*
%{_datadir}/pysol/cardset-maritimes
%{_datadir}/pysol/cardset-melange
%{_datadir}/pysol/cardset-migeon*
%{_datadir}/pysol/cardset-nickel*

%files cardsets-collectors-P-W
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-prince*
%{_datadir}/pysol/cardset-spin*
%{_datadir}/pysol/cardset-tensho
%{_datadir}/pysol/cardset-transformation
%{_datadir}/pysol/cardset-traugott*
%{_datadir}/pysol/cardset-ukiyoe-*
%{_datadir}/pysol/cardset-vienna-2k-small
%{_datadir}/pysol/cardset-vienna-tarock
%{_datadir}/pysol/cardset-wilhelmtell

%files cardsets-fantasy
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-rivers*

%files cardsets-os
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-penguins
%{_datadir}/pysol/cardset-spaced
%{_datadir}/pysol/cardset-tuxedo
%{_datadir}/pysol/cardset-xpat2

%files cardsets-round
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-mughal*
%{_datadir}/pysol/cardset-dashavatara*
%{_datadir}/pysol/cardset-get-a-round
%{_datadir}/pysol/cardset-ovale*

%files cardsets-uncategorized
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-aisleriot
%{_datadir}/pysol/cardset-colossus
%{_datadir}/pysol/cardset-gdkcard-bonded
%{_datadir}/pysol/cardset-gpl
%{_datadir}/pysol/cardset-jacoby
%{_datadir}/pysol/cardset-kabale
%{_datadir}/pysol/cardset-naylor
%{_datadir}/pysol/cardset-oxymoron*
%{_datadir}/pysol/cardset-rangoon*
%{_datadir}/pysol/cardset-spider
%{_datadir}/pysol/cardset-tksol
%{_datadir}/pysol/cardset-xpat2-*

%files sounds
%defattr(644,root,root,755)
%{_datadir}/pysol/sound

%files music
%defattr(644,root,root,755)
%{_datadir}/pysol/music
