from enum import Enum


class Direction(Enum):
    """Represents the direction options for the
    `Movers` service.

    ### Usage
    ----
        >>> from td.enums import Directions
        >>> Directions.Up.value
    """

    Up = 'up'
    Down = 'down'


class Change(Enum):
    """Represents the change options for the
    `Movers` service.

    ### Usage
    ----
        >>> from td.enums import Change
        >>> Change.Percent.value
    """

    Percent = 'percent'
    Value = 'value'


class TransactionTypes(Enum):
    """Represents the types of transaction you
    can query from TD Ameritrade using the `Accounts`
    services.

    ### Usage
    ----
        >>> from td.enums import TransactionTypes
        >>> TransactionTypes.Trade.value
    """

    All = 'ALL'
    Trade = 'TRADE'
    BuyOnly = 'BUY_ONLY'
    SellOnly = 'SELL_ONLY'
    CashInOrCashOut = 'CASH_IN_OR_CASH_OUT'
    Checking = 'CHECKING'
    Dividend = 'DIVIDEND'
    Interest = 'INTEREST'
    Other = 'OTHER'
    AdvisorFees = 'ADVISOR_FEES'


class Markets(Enum):
    """Represents the different markets you can request
    hours for the `MarketHours` service.

    ### Usage
    ----
        >>> from td.enums import Markets
        >>> Markets.Bond.Value
    """

    Bond = 'BOND'
    Equity = 'EQUITY'
    Option = 'OPTION'
    Forex = 'FOREX'
    Futures = 'FUTURES'


class Projections(Enum):
    """Represents the different search types you can use for
    the `Instruments` service.

    ### Usage
    ----
        >>> from td.enums import Projections
        >>> Projections.Bond.Value
    """

    SymbolSearch = 'symbol-search'
    SymbolRegex = 'symbol-regex'
    DescriptionSearch = 'desc-search'
    DescriptionRegex = 'desc-regex'
    Fundamental = 'fundamental'


class DefaultOrderLegInstruction(Enum):
    """Represents the different Default Order Leg Instructions
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultOrderLegInstruction
        >>> DefaultOrderLegInstruction.Sell.Value
    """

    Buy = 'BUY'
    Sell = 'SELL'
    BuyToCover = 'BUY_TO_COVER'
    SellShort = 'SELL_SHORT'
    NoneSpecified = 'NONE'


class DefaultOrderType(Enum):
    """Represents the different Default Order Type
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultOrderType
        >>> DefaultOrderType.Market.Value
    """

    Market = 'MARKET'
    Limit = 'LIMIT'
    Stop = 'STOP'
    StopLimit = 'STOP_LIMIT'
    TrailingStop = 'TRAILING_STOP'
    MarketOnClose = 'MARKET_ON_CLOSE'
    NoneSpecified = 'NONE'


class DefaultOrderPriceLinkType(Enum):
    """Represents the different Default Order Price Link Type
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultOrderPriceLinkType
        >>> DefaultOrderPriceLinkType.Value.Value
    """

    Value = 'VALUE'
    Percent = 'PERCENT'
    NoneSpecified = 'NONE'


class DefaultOrderDuration(Enum):
    """Represents the different Default Order Duration
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultOrderDuration
        >>> DefaultOrderDuration.Day.Value
    """

    Day = 'DAY'
    GoodTillCancel = 'GOOD_TILL_CANCEL'
    FillOrKill = 'FILL_OR_KILL'
    NoneSpecified = 'NONE'


class DefaultOrderMarketSession(Enum):
    """Represents the different Default Order Market Session
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultOrderMarketSession
        >>> DefaultOrderMarketSession.Day.Value
    """

    Am = 'AM'
    Pm = 'PM'
    Normal = 'NORMAL'
    Seamless = 'SEAMLESS'
    NoneSpecified = 'NONE'


class TaxLotMethod(Enum):
    """Represents the different Tax Lot Methods
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import MutualFundTaxLotMethod
        >>> MutualFundTaxLotMethod.Day.Value
    """

    Fifo = 'FIFO'
    Lifo = 'LIFO'
    HighCost = 'HIGH_COST'
    LowCost = 'LOW_COST'
    MinimumTax = 'MINIMUM_TAX'
    AverageCost = 'AVERAGE_COST'
    NoneSpecified = 'NONE'


class DefaultAdvancedToolLaunch(Enum):
    """Represents the different Default Advanced Tool
    Lauch for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultAdvancedToolLaunch
        >>> DefaultAdvancedToolLaunch.Tos.Value
    """

    Ta = 'Ta'
    No = 'N'
    Yes = 'Y'
    Tos = 'TOS'
    Cc2 = 'CC2'
    NoneSpecified = 'NONE'


class AuthTokenTimeout(Enum):
    """Represents the different Auth Token Timeout
    properties for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import AuthTokenTimeout
        >>> AuthTokenTimeout.FiftyFiveMinutes.Value
    """

    FiftyFiveMinutes = 'FIFTY_FIVE_MINUTES'
    TwoHours = 'TWO_HOURS'
    FourHours = 'FOUR_HOURS'
    EightHours = 'EIGHT_HOURS'


class FrequencyType(Enum):
    """Represents the different chart frequencies
    for the `PriceHistory` service.

    ### Usage
    ----
        >>> from td.enums import PriceFrequency
        >>> PriceFrequency.Daily.Value
    """

    Minute = 'minute'
    Daily = 'daily'
    Weekly = 'weekly'
    Monthly = 'monthly'


class PeriodType(Enum):
    """Represents the different chart periods
    for the `PriceHistory` service.

    ### Usage
    ----
        >>> from td.enums import PriceFrequency
        >>> PeriodType.Daily.Value
    """

    Day = 'day'
    Month = 'month'
    Year = 'year'
    YearToDate = 'ytd'


class StrategyType(Enum):
    """Represents the different strategy types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.enums import StrategyType
        >>> StrategyType.Analytical.Value
    """

    Analytical = 'ANALYTICAL'
    Butterfly = 'BUTTERFLY'
    Calendar = 'CALENDAR'
    Collar = 'COLLAR'
    Condor = 'CONDOR'
    Covered = 'COVERED'
    Diagonal = 'DIAGONAL'
    Roll = 'ROLL'
    Single = 'SINGLE'
    Straddle = 'STRADDLE'
    Strangle = 'STRANGLE'
    Vertical = 'VERTICAL'


class OptionaRange(Enum):
    """Represents the different option range types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.enums import OptionaRange
        >>> OptionaRange.InTheMoney.Value
    """

    All = 'ALL'
    InTheMoney = 'ITM'
    NearTheMoney = 'NTM'
    OutTheMoney = 'OTM'
    StrikesAboveMarket = 'SAK'
    StrikesBelowMarket = 'SBK'
    StrikesNearMarket = 'SNK'


class ExpirationMonth(Enum):
    """Represents the different option expiration months
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.enums import ExpirationMonth
        >>> ExpirationMonth.Janurary.Value
    """

    All = 'ALL'
    Janurary = 'JAN'
    Feburary = 'FEB'
    March = 'MAR'
    April = 'April'
    May = 'MAY'
    June = 'JUN'
    July = 'JUL'
    August = 'AUG'
    September = 'SEP'
    October = 'OCT'
    November = 'NOV'
    December = 'DEC'


class ContractType(Enum):
    """Represents the different option contract types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.enums import ContractType
        >>> ContractType.Call.Value
    """

    All = 'ALL'
    Call = 'CALL'
    Put = 'PUT'


class OptionType(Enum):
    """Represents the different option types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.enums import OptionType
        >>> OptionType.Call.Value
    """

    All = 'ALL'
    StandardContracts = 'S'
    NonStandardContracts = 'NS'


class OrderStatus(Enum):
    """Represents the different order status types
    when querying the `Orders` service.

    ### Usage
    ----
        >>> from td.enums import OrderStatus
        >>> OrderStatus.Working.Value
    """

    AwaitingParentOrder = 'AWAITING_PARENT_ORDER'
    AwaitingCondition = 'AWAITING_CONDITION'
    AwaitingManualReview = 'AWAITING_MANUAL_REVIEW'
    Accepted = 'ACCEPTED'
    AwaitingUrOut = 'AWAITING_UR_OUT'
    PendingActivation = 'PENDING_ACTIVATION'
    Queded = 'QUEUED'
    Working = 'WORKING'
    Rejected = 'REJECTED'
    PendingCancel = 'PENDING_CANCEL'
    Canceled = 'CANCELED'
    PendingReplace = 'PENDING_REPLACE'
    Replaced = 'REPLACED'
    Filled = 'FILLED'
    Expired = 'EXPIRED'


class OrderStrategyType(Enum):
    """Represents the different order strategy types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import OrderStrategyType
        >>> OrderStrategyType.Single.Value
    """

    Single = 'SINGLE'
    Oco = 'OCO'
    Trigger = 'TRIGGER'


class QuantityType(Enum):
    """Represents the different order quantity types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import QuantityType
        >>> QuantityType.Dollars.Value
    """

    AllShares = 'ALL_SHARES'
    Dollars = 'DOLLARS'
    Shares = 'SHARES'


class AssetType(Enum):
    """Represents the different order Asset types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import AssetType
        >>> AssetType.Equity.Value
    """

    Equity = 'EQUITY'
    Option = 'OPTION'
    Index = 'INDEX'
    MutualFund = 'MUTUAL_FUND'
    CashEquivalent = 'CASH_EQUIVALENT'
    FixedIncome = 'FIXED_INCOME'
    Currency = 'CURRENCY'


class ComplexOrderStrategyType(Enum):
    """Represents the different order Asset types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import ComplexOrderStrategyType
        >>> ComplexOrderStrategyType.IronCondor.Value
    """

    NoneProvided = 'NONE'
    Covered = 'COVERED'
    Vertical = 'VERTICAL'
    BackRatio = 'BACK_RATIO'
    Calendar = 'CALENDAR'
    Diagonal = 'DIAGONAL'
    Straddle = 'STRADDLE'
    Strangle = 'STRANGLE'
    CollarSynthetic = 'COLLAR_SYNTHETIC'
    Butterfly = 'BUTTERFLY'
    Condor = 'CONDOR'
    IronCondor = 'IRON_CONDOR'
    VerticalRoll = 'VERTICAL_ROLL'
    CollarWithStock = 'COLLAR_WITH_STOCK'
    DoubleDiagonal = 'DOUBLE_DIAGONAL'
    UnbalancedButterfly = 'UNBALANCED_BUTTERFLY'
    UnbalancedCondor = 'UNBALANCED_CONDOR'
    UnbalancedIronCondor = 'UNBALANCED_IRON_CONDOR'
    UnbalancedVerticalRoll = 'UNBALANCED_VERTICAL_ROLL'
    Custom = 'CUSTOM'


class OrderInstructions(Enum):
    """Represents the different order instructions
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import OrderInstructions
        >>> OrderInstructions.SellShort.Value
    """

    Buy = 'BUY'
    Sell = 'SELL'
    BuyToCover = 'BUY_TO_COVER'
    SellShort = 'SELL_SHORT'
    BuyToOpen = 'BUY_TO_OPEN'
    BuyToClose = 'BUY_TO_CLOSE'
    SellToOpen = 'SELL_TO_OPEN'
    SellToClose = 'SELL_TO_CLOSE'
    Exchange = 'EXCHANGE'


class RequestedDestination(Enum):
    """Represents the different order requested
    destinations when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import RequestedDestination
        >>> RequestedDestination.Cboe.Value
    """

    Inet = 'INET'
    EcnArca = 'ECN_ARCA'
    Cboe = 'CBOE'
    Amex = 'AMEX'
    Phlx = 'PHLX'
    Ise = 'ISE'
    Box = 'BOX'
    Nyse = 'NYSE'
    Nasdaq = 'NASDAQ'
    Bats = 'BATS'
    C2 = 'C2'
    Auto = 'AUTO'


class StopPriceLinkBasis(Enum):
    """Represents the different stop price link basis 
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import StopPriceLinkBasis
        >>> StopPriceLinkBasis.Trigger.Value
    """

    Manual = 'MANUAL'
    Base = 'BASE'
    Trigger = 'TRIGGER'
    Last = 'LAST'
    Bid = 'BID'
    Ask = 'ASK'
    AskBid = 'ASK_BID'
    Mark = 'MARK'
    Average = 'AVERAGE'


class StopPriceLinkType(Enum):
    """Represents the different stop price link type 
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import StopPriceLinkType
        >>> StopPriceLinkType.Trigger.Value
    """

    Value = 'VALUE'
    Percent = 'PERCENT'
    Tick = 'TICK'


class StopType(Enum):
    """Represents the different stop type 
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import StopType
        >>> StopType.Standard.Value
    """

    Standard = 'STANDARD'
    Bid = 'BID'
    Ask = 'ASK'
    Last = 'LAST'
    Mark = 'MARK'


class PriceLinkBasis(Enum):
    """Represents the different price link basis 
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import PriceLinkBasis
        >>> PriceLinkBasis.Manual.Value
    """

    Manual = 'MANUAL'
    Base = 'BASE'
    Trigger = 'TRIGGER'
    Last = 'LAST'
    Bid = 'BID'
    Ask = 'ASK'
    AskBid = 'ASK_BID'
    Mark = 'MARK'
    Average = 'AVERAGE'


class PriceLinkType(Enum):
    """Represents the different price link type 
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import PriceLinkType
        >>> PriceLinkType.Trigger.Value
    """

    Value = 'VALUE'
    Percent = 'PERCENT'
    Tick = 'TICK'


class OrderType(Enum):
    """Represents the different order type 
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import OrderType
        >>> OrderType.Market.Value
    """

    Market = 'MARKET'
    Limit = 'LIMIT'
    Stop = 'STOP'
    StopLimit = 'STOP_LIMIT'
    TrailingStop = 'TRAILING_STOP'
    MarketOnClose = 'MARKET_ON_CLOSE'
    Exercise = 'EXERCISE'
    TrailingStopLimit = 'TRAILING_STOP_LIMIT'
    NetDebit = 'NET_DEBIT'
    NetCredit = 'NET_CREDIT'
    NetZero = 'NET_ZERO'


class PositionEffect(Enum):
    """Represents the different position effects 
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import PositionEffect
        >>> PositionEffect.Opening.Value
    """

    Opening = 'OPENING'
    Closing = 'CLOSING'
    Automatic = 'AUTOMATIC'


class OrderTaxLotMethod(Enum):
    """Represents the different order tax lot methods 
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import OrderTaxLotMethod
        >>> OrderTaxLotMethod.Fifo.Value
    """

    Fifo = 'FIFO'
    Lifo = 'LIFO'
    HighCost = 'HIGH_COST'
    LowCost = 'LOW_COST'
    AverageCost = 'AVERAGE_COST'
    SpecificLot = 'SPECIFIC_LOT'


class SpecialInstructions(Enum):
    """Represents the different order special instructions 
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.enums import SpecialInstructions
        >>> SpecialInstructions.AllOrNone.Value
    """

    AllOrNone = 'ALL_OR_NONE'
    DoNotReduce = 'DO_NOT_REDUCE'
    AllOrNoneDoNotReduce = 'ALL_OR_NONE_DO_NOT_REDUCE'