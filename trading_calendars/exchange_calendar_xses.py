from datetime import time
import pandas as pd
from pytz import timezone
from .precomputed_trading_calendar import PrecomputedTradingCalendar

precomputed_ses_holidays = pd.to_datetime([
    "1986-01-01",
    "1986-02-10",
    "1986-02-11",
    "1986-03-28",
    "1986-05-01",
    "1986-05-23",
    "1986-06-09",
    "1986-12-25",
    "1987-01-01",
    "1987-01-29",
    "1987-01-30",
    "1987-05-01",
    "1987-05-12",
    "1987-05-29",
    "1987-08-05",
    "1987-08-10",
    "1987-10-21",
    "1987-12-25",
    "1988-01-01",
    "1988-02-17",
    "1988-02-18",
    "1988-04-01",
    "1988-05-02",
    "1988-05-17",
    "1988-05-30",
    "1988-07-25",
    "1988-08-09",
    "1988-11-08",
    "1988-12-26",
    "1989-01-02",
    "1989-02-06",
    "1989-02-07",
    "1989-03-24",
    "1989-05-01",
    "1989-05-08",
    "1989-05-19",
    "1989-07-13",
    "1989-08-09",
    "1989-12-25",
    "1990-01-01",
    "1990-04-13",
    "1990-04-26",
    "1990-05-01",
    "1990-05-09",
    "1990-07-03",
    "1990-08-09",
    "1990-12-25",
    "1991-01-01",
    "1991-01-15",
    "1991-03-29",
    "1991-04-16",
    "1991-05-01",
    "1991-05-28",
    "1991-06-24",
    "1991-08-09",
    "1991-11-05",
    "1991-12-24",
    "1991-12-25",
    "1991-12-31",
    "1992-01-01",
    "1992-02-04",
    "1992-02-05",
    "1992-04-06",
    "1992-04-17",
    "1992-05-01",
    "1992-06-11",
    "1992-08-10",
    "1992-12-25",
    "1993-01-01",
    "1993-01-25",
    "1993-03-25",
    "1993-04-09",
    "1993-05-06",
    "1993-06-01",
    "1993-08-09",
    "1994-01-10",
    "1994-01-11",
    "1994-02-01",
    "1994-02-11",
    "1994-03-14",
    "1994-04-01",
    "1994-05-02",
    "1994-05-25",
    "1994-08-09",
    "1994-10-13",
    "1994-11-02",
    "1994-12-26",
    "1995-01-02",
    "1995-01-31",
    "1995-02-01",
    "1995-03-03",
    "1995-04-14",
    "1995-05-01",
    "1995-05-10",
    "1995-05-15",
    "1995-08-09",
    "1995-10-23",
    "1995-12-25",
    "1996-01-01",
    "1996-02-19",
    "1996-02-20",
    "1996-02-21",
    "1996-04-05",
    "1996-05-01",
    "1996-05-31",
    "1996-08-09",
    "1996-12-25",
    "1997-01-01",
    "1997-02-07",
    "1997-02-10",
    "1997-03-28",
    "1997-04-18",
    "1997-05-01",
    "1997-05-21",
    "1997-12-25",
    "1998-01-01",
    "1998-01-28",
    "1998-01-29",
    "1998-01-30",
    "1998-04-07",
    "1998-04-10",
    "1998-05-01",
    "1998-05-11",
    "1998-08-10",
    "1998-10-19",
    "1998-12-25",
    "1999-01-01",
    "1999-01-19",
    "1999-02-16",
    "1999-02-17",
    "1999-03-29",
    "1999-04-02",
    "1999-08-09",
    "1999-11-08",
    "1999-12-31",
    "2000-02-07",
    "2000-03-16",
    "2000-04-21",
    "2000-05-01",
    "2000-05-18",
    "2000-08-09",
    "2000-10-26",
    "2000-12-25",
    "2000-12-27",
    "2001-01-01",
    "2001-01-24",
    "2001-01-25",
    "2001-03-06",
    "2001-04-13",
    "2001-05-01",
    "2001-05-07",
    "2001-08-09",
    "2001-11-14",
    "2001-12-17",
    "2001-12-25",
    "2002-01-01",
    "2002-02-12",
    "2002-02-13",
    "2002-03-29",
    "2002-05-01",
    "2002-05-27",
    "2002-08-09",
    "2002-11-04",
    "2002-12-06",
    "2002-12-25",
    "2003-01-01",
    "2003-02-03",
    "2003-02-12",
    "2003-04-18",
    "2003-05-01",
    "2003-05-15",
    "2003-10-24",
    "2003-11-25",
    "2003-12-25",
    "2004-01-01",
    "2004-01-22",
    "2004-01-23",
    "2004-02-02",
    "2004-04-09",
    "2004-06-02",
    "2004-08-09",
    "2004-11-11",
    "2004-11-15",
    "2005-01-21",
    "2005-02-09",
    "2005-02-10",
    "2005-03-25",
    "2005-05-02",
    "2005-05-23",
    "2005-08-09",
    "2005-11-01",
    "2005-11-03",
    "2005-12-26",
    "2006-01-02",
    "2006-01-10",
    "2006-01-30",
    "2006-01-31",
    "2006-04-14",
    "2006-05-01",
    "2006-05-12",
    "2006-08-09",
    "2006-10-24",
    "2006-12-25",
    "2007-01-01",
    "2007-01-02",
    "2007-02-19",
    "2007-02-20",
    "2007-04-06",
    "2007-05-01",
    "2007-05-31",
    "2007-08-09",
    "2007-11-08",
    "2007-12-20",
    "2007-12-25",
    "2008-01-01",
    "2008-02-07",
    "2008-02-08",
    "2008-03-21",
    "2008-05-01",
    "2008-05-19",
    "2008-10-01",
    "2008-10-27",
    "2008-12-08",
    "2008-12-25",
    "2009-01-01",
    "2009-01-26",
    "2009-01-27",
    "2009-04-10",
    "2009-05-01",
    "2009-08-10",
    "2009-09-21",
    "2009-11-27",
    "2009-12-25",
    "2010-01-01",
    "2010-02-15",
    "2010-02-16",
    "2010-04-02",
    "2010-05-28",
    "2010-08-09",
    "2010-09-10",
    "2010-11-05",
    "2010-11-17",
    "2011-02-03",
    "2011-02-04",
    "2011-04-22",
    "2011-05-02",
    "2011-05-17",
    "2011-08-09",
    "2011-08-30",
    "2011-10-26",
    "2011-11-07",
    "2011-12-26",
    "2012-01-02",
    "2012-01-23",
    "2012-01-24",
    "2012-04-06",
    "2012-05-01",
    "2012-08-09",
    "2012-08-20",
    "2012-10-26",
    "2012-11-13",
    "2012-12-25",
    "2013-01-01",
    "2013-02-11",
    "2013-02-12",
    "2013-03-29",
    "2013-05-01",
    "2013-05-24",
    "2013-08-08",
    "2013-08-09",
    "2013-10-15",
    "2013-12-25",
    "2014-01-01",
    "2014-01-31",
    "2014-04-18",
    "2014-05-01",
    "2014-05-13",
    "2014-07-28",
    "2014-10-06",
    "2014-10-22",
    "2014-12-25",
    "2015-01-01",
    "2015-02-19",
    "2015-02-20",
    "2015-04-03",
    "2015-05-01",
    "2015-06-01",
    "2015-07-17",
    "2015-08-07",
    "2015-08-10",
    "2015-09-11",
    "2015-09-24",
    "2015-11-10",
    "2015-12-25",
    "2016-01-01",
    "2016-02-08",
    "2016-02-09",
    "2016-03-25",
    "2016-05-02",
    "2016-07-06",
    "2016-08-09",
    "2016-09-12",
    "2016-12-26",
    "2017-01-02",
    "2017-01-30",
    "2017-04-14",
    "2017-05-01",
    "2017-05-10",
    "2017-06-26",
    "2017-08-09",
    "2017-09-01",
    "2017-10-18",
    "2017-12-25",
    "2018-01-01",
    "2018-02-16",
    "2018-03-30",
    "2018-05-01",
    "2018-05-29",
    "2018-06-15",
    "2018-08-09",
    "2018-08-22",
    "2018-11-06",
    "2018-12-25",
    "2019-01-01",
    "2019-02-05",
    "2019-02-06",
    "2019-04-19",
    "2019-05-01",
    "2019-05-20",
    "2019-06-05",
    "2019-08-09",
    "2019-12-15",
    "2020-01-01",
    "2020-01-27",
    "2020-04-10",
    "2020-05-01",
    "2020-05-07",
    "2020-05-24",
    "2020-07-31",
    "2020-12-25",
])


class XSESExchangeCalendar(PrecomputedTradingCalendar):
    """
    Exchange calendar for the Singapore Stock Exchange (XSES, SGX).

    Open time: 9:00 Asia/Singapore
    Close time: 17:00 Asia/Singapore

    NOTE: For now, we are skipping the intra-day break from 12:00 to 13:00.

    Due to the complexity around the Singaporean holidays, we are hardcoding
    a list of holidays covering 1986-2020, inclusive.

    TODO: There are a handful of half-days (day before Chinese New Year,
    Christmas Eve, etc.). We will add those later.
    """

    name = "XSES"
    tz = timezone("Asia/Singapore")
    open_times = (
        (None, time(9, 1)),
    )
    close_times = (
        (None, time(15, 0)),
    )

    @property
    def precomputed_holidays(self):
        return precomputed_ses_holidays
