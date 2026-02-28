const translations = {
    // Navbar
    'nav.home': { uz: 'Bosh sahifa', en: 'Home' },
    'nav.catalog': { uz: 'Katalog', en: 'Catalog' },
    'nav.about': { uz: 'Biz haqimizda', en: 'About us' },
    'nav.login': { uz: 'Kirish', en: 'Login' },
    'nav.register': { uz: "Ro'yxatdan o'tish", en: 'Register' },

    // Hero
    'hero.title': { uz: "Bilim olish — eng ulug' ibodat", en: 'Knowledge is the greatest worship' },
    'hero.subtitle': { uz: "603+ kitob, 37 eKitob, raqamli resurslar va ilmiy bazalar bir joyda", en: '603+ books, 37 eBooks, digital resources and scientific databases in one place' },
    'hero.placeholder': { uz: "Kitob nomi, muallif yoki ISBN qidiring...", en: 'Search by book title, author or ISBN...' },
    'hero.search': { uz: 'Qidirish', en: 'Search' },

    // Stats
    'stats.physicalBooks': { uz: 'Jismoniy kitoblar', en: 'Physical books' },
    'stats.ebooks': { uz: 'eKitoblar', en: 'eBooks' },
    'stats.books': { uz: 'Kitoblar', en: 'Books' },
    'stats.authors': { uz: 'Mualliflar', en: 'Authors' },
    'stats.categories': { uz: 'Kategoriyalar', en: 'Categories' },

    // Sections
    'section.categories': { uz: 'Kategoriyalar', en: 'Categories' },
    'section.viewAll': { uz: "Barchasini ko'rish", en: 'View all' },
    'section.newBooks': { uz: "Yangi qo'shilgan kitoblar", en: 'Newly added books' },
    'section.popularBooks': { uz: 'Mashhur kitoblar', en: 'Popular books' },
    'section.relatedBooks': { uz: "O'xshash kitoblar", en: 'Related books' },
    'book.count': { uz: 'kitob', en: 'books' },

    // Footer
    'footer.desc': { uz: "Bilim va ilm-fan markazi. Studentlar uchun eng yaxshi ta'lim resurslari.", en: 'Center of knowledge and science. The best educational resources for students.' },
    'footer.quickLinks': { uz: 'Tezkor havolalar', en: 'Quick links' },
    'footer.categories': { uz: 'Kategoriyalar', en: 'Categories' },
    'footer.programming': { uz: 'Dasturlash', en: 'Programming' },
    'footer.math': { uz: 'Matematika', en: 'Mathematics' },
    'footer.physics': { uz: 'Fizika', en: 'Physics' },
    'footer.literature': { uz: 'Adabiyot', en: 'Literature' },
    'footer.contact': { uz: "Bog'lanish", en: 'Contact' },
    'footer.address': { uz: "Toshkent, O'zbekiston", en: 'Tashkent, Uzbekistan' },
    'footer.workHours': { uz: 'Dush-Jum: 09:00 - 21:00', en: 'Mon-Fri: 09:00 - 21:00' },
    'footer.copyright': { uz: 'AUT E-Library. Barcha huquqlar himoyalangan.', en: 'AUT E-Library. All rights reserved.' },

    // Catalog
    'catalog.breadcrumb': { uz: 'Katalog', en: 'Catalog' },
    'catalog.search': { uz: 'Qidirish', en: 'Search' },
    'catalog.searchPlaceholder': { uz: 'Qidirish...', en: 'Search...' },
    'catalog.categories': { uz: 'Kategoriyalar', en: 'Categories' },
    'catalog.all': { uz: 'Barchasi', en: 'All' },
    'catalog.language': { uz: 'Til', en: 'Language' },
    'catalog.booksFound': { uz: 'kitob topildi', en: 'books found' },
    'catalog.sort': { uz: 'Saralash:', en: 'Sort:' },
    'catalog.newest': { uz: 'Yangilari', en: 'Newest' },
    'catalog.oldest': { uz: 'Eskilari', en: 'Oldest' },
    'catalog.byName': { uz: "Nomi bo'yicha", en: 'By name' },
    'catalog.popular': { uz: 'Mashhur', en: 'Popular' },
    'catalog.rating': { uz: 'Reyting', en: 'Rating' },
    'catalog.noBooks': { uz: 'Kitob topilmadi', en: 'No books found' },
    'catalog.noBooksSub': { uz: "Boshqa so'z bilan qidirib ko'ring yoki filterlarni o'zgartiring", en: 'Try searching with different keywords or change filters' },
    'catalog.allBooks': { uz: 'Barcha kitoblar', en: 'All books' },

    // Book Detail
    'detail.language': { uz: 'Til:', en: 'Language:' },
    'detail.pages': { uz: 'Sahifalar:', en: 'Pages:' },
    'detail.year': { uz: 'Nashr yili:', en: 'Published:' },
    'detail.publisher': { uz: 'Nashriyot:', en: 'Publisher:' },
    'detail.views': { uz: "Ko'rishlar:", en: 'Views:' },
    'detail.download': { uz: 'PDF yuklab olish', en: 'Download PDF' },
    'detail.addFavorite': { uz: "Sevimlilarga qo'shish", en: 'Add to favorites' },
    'detail.removeFavorite': { uz: "Sevimlilardan o'chirish", en: 'Remove from favorites' },
    'detail.description': { uz: 'Tavsif', en: 'Description' },
    'detail.review': { uz: 'sharh', en: 'reviews' },

    // Reviews
    'review.title': { uz: 'Sharhlar', en: 'Reviews' },
    'review.leave': { uz: 'Sharh qoldiring', en: 'Leave a review' },
    'review.score': { uz: 'Baho', en: 'Rating' },
    'review.placeholder': { uz: 'Kitob haqida fikringizni yozing...', en: 'Write your opinion about the book...' },
    'review.submit': { uz: 'Yuborish', en: 'Submit' },
    'review.loginRequired': { uz: 'Sharh qoldirish uchun', en: 'To leave a review' },
    'review.loginLink': { uz: 'tizimga kiring', en: 'please login' },
    'review.empty': { uz: "Hali sharhlar yo'q. Birinchi bo'lib sharh qoldiring!", en: 'No reviews yet. Be the first to leave a review!' },
    'review.ago': { uz: 'oldin', en: 'ago' },

    // Auth
    'auth.login': { uz: 'Kirish', en: 'Login' },
    'auth.loginSubtitle': { uz: 'E-Library tizimiga kirish', en: 'Login to the E-Library system' },
    'auth.loginError': { uz: "Foydalanuvchi nomi yoki parol noto'g'ri.", en: 'Invalid username or password.' },
    'auth.username': { uz: 'Foydalanuvchi nomi', en: 'Username' },
    'auth.usernamePlaceholder': { uz: 'Username kiriting', en: 'Enter username' },
    'auth.password': { uz: 'Parol', en: 'Password' },
    'auth.passwordPlaceholder': { uz: 'Parol kiriting', en: 'Enter password' },
    'auth.loginBtn': { uz: 'Kirish', en: 'Login' },
    'auth.noAccount': { uz: "Akkauntingiz yo'qmi?", en: "Don't have an account?" },
    'auth.registerLink': { uz: "Ro'yxatdan o'ting", en: 'Register' },
    'auth.register': { uz: "Ro'yxatdan o'tish", en: 'Register' },
    'auth.registerSubtitle': { uz: 'Yangi akkaunt yarating', en: 'Create a new account' },
    'auth.registerBtn': { uz: "Ro'yxatdan o'tish", en: 'Register' },
    'auth.hasAccount': { uz: 'Akkauntingiz bormi?', en: 'Already have an account?' },

    // Profile
    'profile.noEmail': { uz: "Email ko'rsatilmagan", en: 'Email not specified' },
    'profile.memberSince': { uz: "dan beri a'zo", en: 'member since' },
    'profile.favorites': { uz: 'Sevimlilar', en: 'Favorites' },
    'profile.myReviews': { uz: 'Sharhlarim', en: 'My reviews' },
    'profile.noFavorites': { uz: "Sevimli kitoblaringiz yo'q", en: 'You have no favorite books' },
    'profile.goToCatalog': { uz: "Katalogga o'tish", en: 'Go to catalog' },
    'profile.noReviews': { uz: 'Hali sharh qoldirmagansiz', en: "You haven't left any reviews yet" },
    'profile.viewBooks': { uz: "Kitoblarni ko'rish", en: 'View books' },
    'profile.delete': { uz: "O'chirish", en: 'Remove' },

    // About
    'about.title': { uz: 'Biz haqimizda', en: 'About us' },
    'about.subtitle': { uz: "AUT E-Library — bilim, ilm-fan va zamonaviy ta'lim resurslari markazi", en: 'AUT E-Library — center for knowledge, science and modern educational resources' },
    'about.heading': { uz: 'E-Library haqida', en: 'About the E-Library' },
    'about.p1': { uz: "AUT E-Library universitetimizning markaziy bilim markazi bo'lib, jismoniy fondda 603 ta kitob va 37 ta eKitob mavjud. E-Library studentlar, o'qituvchilar va tadqiqotchilar uchun keng qamrovli ta'lim resurslari taqdim etadi.", en: 'AUT E-Library is the central knowledge hub of our university, with a physical collection of 603 books and 37 eBooks. Our E-Library provides comprehensive educational resources for students, teachers and researchers.' },
    'about.p2': { uz: "Kitoblarni qarz olish uchun kutubxona a'zosi bo'lish kerak. Har bir a'zo bir vaqtning o'zida 3 tagacha kitob olishi mumkin. Kitoblar 14 kun muddatga beriladi, muddatni bir marta 7 kunga uzaytirish mumkin.", en: 'To borrow books, you must be a library member. Each member can borrow up to 3 books at a time. Books are issued for 14 days, with a one-time 7-day extension available.' },
    'about.rulesTitle': { uz: 'Kutubxona qoidalari', en: 'Library Rules' },
    'about.rule1': { uz: "Kutubxonaga ro'yxatdan o'tish uchun talaba guvohnomasi yoki xodim ID kartasi talab qilinadi.", en: 'A student ID or staff ID card is required for library registration.' },
    'about.rule2': { uz: "Kitoblar 14 kun muddatga beriladi. Muddatni bir marta 7 kunga uzaytirish mumkin.", en: 'Books are issued for 14 days. The period can be extended once for 7 days.' },
    'about.rule3': { uz: "Muddatidan kechiktirilgan har bir kun uchun 1,000 so'm jarima belgilanadi.", en: 'A fine of 1,000 UZS is charged for each overdue day.' },
    'about.rule4': { uz: "Kutubxonaga shaxsiy sumkalar bilan kirilmaydi — maxsus shkafchalar mavjud.", en: 'Personal bags are not allowed in the library — lockers are available.' },
    'about.rule5': { uz: "O'qish zalida ovqatlanish va baland ovozda gaplashish taqiqlanadi.", en: 'Eating and loud talking are prohibited in the reading hall.' },
    'about.rule6': { uz: "Yo'qolgan yoki shikastlangan kitob uchun to'liq qiymati qoplanadi.", en: 'Lost or damaged books must be compensated at full value.' },
    'about.helpTitle': { uz: 'Yordam', en: 'Help' },
    'about.helpDesc': { uz: "Kutubxonachilarimiz sizga kerakli kitobni topish, raqamli resurslardan foydalanish va ilmiy tadqiqotlar uchun manba izlashda yordam beradi. Telegram bot orqali ham yordam olishingiz mumkin: @AI_librarianbot", en: 'Our librarians will help you find the right book, use digital resources and search for sources for scientific research. You can also get help via Telegram bot: @AI_librarianbot' },
    'about.bookClubTitle': { uz: 'Book Club', en: 'Book Club' },
    'about.bookClubDesc': { uz: "Har 2 haftada bir kitob tanlanadi va guruh a'zolari orasida munozara o'tkaziladi. Kitob klubi — bu bilim almashish, yangi g'oyalar kashf etish va o'qish madaniyatini rivojlantirish uchun ajoyib imkoniyat.", en: 'Every 2 weeks a book is selected and discussed among group members. The book club is a great opportunity for sharing knowledge, discovering new ideas and developing a reading culture.' },
    'about.bookClubJoin': { uz: "Ro'yxatdan o'tish uchun kutubxonaga murojaat qiling yoki Telegram bot orqali yozing.", en: 'To register, visit the library or write via Telegram bot.' },
    'about.digitalTitle': { uz: 'Raqamli resurslar', en: 'Digital Resources' },
    'about.digitalDesc': { uz: "AUT kutubxonasi a'zolari quyidagi raqamli resurslarga bepul kirish huquqiga ega:", en: 'AUT library members have free access to the following digital resources:' },
    'about.acmDesc': { uz: "Kompyuter fanlari bo'yicha dunyodagi eng katta raqamli kutubxona.", en: "The world's largest digital library for computing and information technology." },
    'about.britannicaDesc': { uz: "Ilmiy maqolalar, multimedia va ishonchli ma'lumotnoma.", en: 'Scientific articles, multimedia and trusted reference materials.' },
    'about.elibraryDesc': { uz: "AQSh elchixonasi tomonidan taqdim etilgan elektron kutubxona.", en: 'Electronic library provided by the US Embassy.' },
    'about.freePlatformsTitle': { uz: "Bepul ta'lim platformalari", en: 'Free Educational Platforms' },
    'about.freePlatformsDesc': { uz: "Quyidagi ochiq ta'lim platformalaridan bepul foydalanishingiz mumkin:", en: 'You can use the following open educational platforms for free:' },
    'about.bccampusDesc': { uz: "Ochiq darsliklar va ta'lim resurslari platformasi.", en: 'Open textbooks and educational resources platform.' },
    'about.mitDesc': { uz: "MIT universitetining bepul ochiq kurslari va materiallari.", en: "MIT university's free open courses and materials." },
    'about.oerDesc': { uz: "Muhandislik sohasidagi ochiq ta'lim resurslari.", en: 'Open educational resources in engineering.' },
    'about.intlTitle': { uz: 'Xalqaro ochiq kutubxonalar va bazalar', en: 'International Open Libraries and Databases' },
    'about.intlDesc': { uz: "Quyidagi xalqaro platformalarda millionlab kitob va ilmiy maqolalarga bepul kirish mumkin:", en: 'Free access to millions of books and scientific articles on the following international platforms:' },
    'about.physicalBooks': { uz: 'Jismoniy kitoblar', en: 'Physical books' },
    'about.ebooks': { uz: 'eKitoblar', en: 'eBooks' },
    'about.workHours': { uz: 'Ish vaqti', en: 'Working hours' },
    'about.schedule': { uz: 'Dush-Jum: 09:00 - 21:00', en: 'Mon-Fri: 09:00 - 21:00' },
    'about.weekendClosed': { uz: 'Shanba-Yakshanba: Dam olish', en: 'Sat-Sun: Closed' },
    'about.inNumbers': { uz: 'Raqamlarda', en: 'In numbers' },
    'about.totalBooks': { uz: 'Jami kitoblar', en: 'Total books' },
    'about.totalCategories': { uz: 'Kategoriyalar', en: 'Categories' },
    'about.totalAuthors': { uz: 'Mualliflar', en: 'Authors' },
    'about.contact': { uz: "Bog'lanish", en: 'Contact' },
};

function setLanguage(lang) {
    localStorage.setItem('siteLang', lang);
    applyLanguage(lang);
}

function applyLanguage(lang) {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[key] && translations[key][lang]) {
            el.textContent = translations[key][lang];
        }
    });
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (translations[key] && translations[key][lang]) {
            el.placeholder = translations[key][lang];
        }
    });
    document.querySelectorAll('[data-i18n-title]').forEach(el => {
        const key = el.getAttribute('data-i18n-title');
        if (translations[key] && translations[key][lang]) {
            el.title = translations[key][lang];
        }
    });

    // Update switcher active state
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === lang);
    });

    document.documentElement.lang = lang === 'uz' ? 'uz' : 'en';
}

document.addEventListener('DOMContentLoaded', function() {
    const lang = localStorage.getItem('siteLang') || 'en';
    applyLanguage(lang);

    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            setLanguage(this.dataset.lang);
        });
    });
});
