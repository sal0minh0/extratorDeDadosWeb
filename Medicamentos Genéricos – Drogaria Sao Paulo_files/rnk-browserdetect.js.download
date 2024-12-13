window.BrowserDetect = {
    init: function () {
        try {
            const browser = this.getNavigator();
            this.browser = browser.name;
            this.version = browser.version;
            this.os = this.searchString(this.dataOS) || 'Unknown';
            this.mobile = /Mobile|mini|Fennec|Android|iP(ad|od|hone)/.test(navigator.appVersion);
            document.body.classList.add('browser-' + this.browser.toLowerCase());
            document.body.classList.add('browser-version-' + this.version);
            document.body.classList.add('mobile-' + this.mobile);
            document.body.classList.add('os-' + this.os.toLowerCase());
        } catch (error) {
            console.log(error);
        }
    },
    searchString: function (data) {
        for (var i = 0; i < data.length; i++) {
            var dataString = data[i].string;
            this.versionSearchString = data[i].subString;
            
            if (dataString.indexOf(data[i].subString) !== -1) {
                return data[i].identity;
            }
        }
    },
    getNavigator: function () {
        var ua = navigator.userAgent,
        tem,
        M = ua.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i) || [];
        if (/trident/i.test(M[1])) {
            tem = /\brv[ :]+(\d+)/g.exec(ua) || [];
            return { name: 'IE', version: tem[1] || '' };
        }
        if (M[1] === 'Chrome') {
            tem = ua.match(/\bOPR|Edge\/(\d+)/);
            if (tem != null) {
                return { name: 'Opera', version: tem[1] };
            }
        }
        M = M[2] ? [M[1], M[2]] : [navigator.appName, navigator.appVersion, '-?'];
        if ((tem = ua.match(/version\/(\d+)/i)) != null) {
            M.splice(1, 1, tem[1]);
        }
        
        return {
            name: M[0],
            version: M[1],
        };
    },
    dataOS: [
        {
            string: navigator.platform,
            subString: 'Win',
            identity: 'Windows',
        },
        {
            string: navigator.platform,
            subString: 'Mac',
            identity: 'macOS',
        },
        {
            string: navigator.userAgent,
            subString: 'iPhone',
            identity: 'iOS',
        },
        {
            string: navigator.userAgent,
            subString: 'iPad',
            identity: 'iOS',
        },
        {
            string: navigator.userAgent,
            subString: 'iPod',
            identity: 'iOS',
        },
        {
            string: navigator.userAgent,
            subString: 'Android',
            identity: 'Android',
        },
        {
            string: navigator.platform,
            subString: 'Linux',
            identity: 'Linux',
        },
    ],
};

BrowserDetect.init();
