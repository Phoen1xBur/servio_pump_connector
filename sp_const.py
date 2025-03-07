""" Константы """
""" Разделитель целой и дробной части """
DefaultDecimalSeparator = '.'
""" Формат даты """
DefaultDateFormat = 'dd/MM/yyyy'
""" Разделитель полей даты """
DefaultDateSeparator = '.'
""" Формат веремени """
DefaultTimeFormat = 'hh:nn:ss.zzz'
""" Разделитель полей времени """
DefaultTimeSeparator = ':'
""" Формат даты/времени """
DefaultDateTimeFormat = 'dd/MM/yyyy hh:nn:ss.zzz'
""" Значение неуказанной даты-времени """
NullDateTime = 0
""" Ограничение при выдаче записей по-умолчанию """
DefaultLimit = 20000
""" Максимальная длина идентификатора запроса (см. TAG_REQUEST_ID) """
MaxRequestIdLen = 32
""" Максимальное кол-во уникальных идентификаторов запроса """
MaxUniqueRequestIds = 10000
""" Максимальный объем POST-данных HTTP(s) сервера, байт """
MaxPostStreamSize = 1048576

""" Тип скидки. см. тэг DiscountType """
""" Нет скидки """
DT_NONE            = 0
""" Скидка с цены в процентах """
DT_PRICE_PERCENT   = 1
""" Скидка с цены в рублях """
DT_PRICE_ABSOLUTE  = 2
""" Фиксированная цена """
DT_FIXED_PRICE     = 3
""" Округление до предзаказа """
DT_ROUND_TO_PRESET = 7

""" Тип скидки дисконтной схемы """
""" Скидка с цены в процентах """
DISCOUNT_KIND_PRICE_PERCENT     = '%'
""" Скидка с цены в абсолютном выражении """
DISCOUNT_KIND_PRICE_ABSOLUTE    = '$'
""" Фиксированная цена """
DISCOUNT_KIND_FIXED_PRICE       = 'F'

""" Вид оплаты, см. тэг PaymentKind """
""" оплата наличными """
PK_CASH     = 0
""" безналичная оплата"""
PK_CASHLESS = 1

""" Коды операций терминала """
""" Оплата """
OP_PAYMENT_PREPARE    =  0
""" Подтверждение оплаты """
OP_PAYMENT_CONFIRM    =  1
""" Возврат """
OP_RETURN_PREPARE     =  2
""" Подтверждение возврата """
OP_RETURN_CONFIRM     =  3
""" Коррекция """
OP_CORRECTION_PREPARE =  4
""" Подтверждение коррекции """
OP_CORRECTION_CONFIRM =  5
""" Пополнение """
OP_CREDIT_PREPARE     =  6
""" Подтверждение пополнения """
OP_CREDIT_CONFIRM     =  7
""" Открытие смены на терминале """
OP_SHIFT_OPEN         =  8
""" Закрытие смены на терминале """
OP_SHIFT_CLOSE        =  9
""" Получение информации по карте """
OP_CARD_INFO          = 10
""" Установка заказа на ТРК """
OP_PRESET             = 11
""" Сброс состояния (отмена транзакции) """
OP_RESET              = 12
""" Аварийный возврат (сброс заказа) """
OP_EMERGENCY_RETURN   = 13
""" Транзакция завершена """
OP_COMPLETED          = 14
""" Транзакция отменена """
OP_CANCELED           = 15

""" Тип позиции """
""" Товар """
GK_GOOD    = 0
""" Услуга """
GK_SERVICE = 1
""" Топливо """
GK_FUEL    = 2
""" Группа товаров/услуг """
GK_GROUP   = 3

""" Режим заказа ТРК """
""" Объем """
SLT_VOLUME        = 0
""" Сумма """
SLT_MONEY         = 1
""" Без ограничения """
SLT_UNLIMITED     = 2

""" Статусы ТРК """
""" простой, ТРК работоспособна, в режиме ожидания заказа """
FPS_IDLE          =  0
""" ТРК заблокирована """
FPS_LOCKED        =  1
""" ТРК в нарботоспособном состоянии """
FPS_DOWN          =  2
""" на ТРК идет отпуск топлива """
FPS_FUELLING      =  3
""" на ТРК снят пистолет, ТРК работоспособна, в режиме ожидания заказа """
FPS_NOZZUP        =  4
""" нет свзи с ТРК """
FPS_COMMOFF       =  5
""" связь с ТРК отключена (ТРК не опрашивается программой) """
FPS_SWITCHEDOFF   =  6
""" на ТРК окончен отпуск топлива, ожидание платежа """
FPS_ENDOFFUELLING =  7
""" ТРК используется другим оператором """
FPS_NONE          =  8
""" ТРК Остановлена """
FPS_STOPPED       =  9
""" Заказ установлен """
FPS_ORDERREADY    = 10

""" Схемы расписаний """
""" Каждый день """
SCHEDULE_SCHEME_EVERYDAY         = 'everyday'
""" По рабочим дням """
SCHEDULE_SCHEME_WORKING_DAYS     = 'working_days'
""" По выходным дням и праздникам """
SCHEDULE_SCHEME_HOLIDAYS         = 'holidays'
""" Выбранные дни недели """
SCHEDULE_SCHEME_CHOOSEN_WEEKDAYS = 'choosen_week_days'
""" Диапазон дат """
SCHEDULE_SCHEME_DATES_RANGE      = 'dates_range'
""" Четные дни """
SCHEDULE_SCHEME_EVEN_DAYS        = 'even_days'
""" Нечетные дни """
SCHEDULE_SCHEME_ODD_DAYS         = 'odd_days'

""" Выбранные дни недели расписаний """
""" Понедельник """
WEEKDAY_MONDAY    = 'monday'
""" Вторник """
WEEKDAY_TUESDAY   = 'tuesday'
""" Среда """
WEEKDAY_WEDNESDAY = 'wednesdeay'
""" Четверг """
WEEKDAY_THURSDAY  = 'thursday'
""" Пятница """
WEEKDAY_FRIDAY    = 'friday'
""" Суббота """
WEEKDAY_SATURDAY  = 'saturday'
""" Воскресенье """
WEEKDAY_SUNDAY    = 'sunday'

""" Коды текущего состояния транзакции """
""" ТРК выполняет заказ """
TRANS_RESULT_FOUND_ON_DISPENSER       = 'FoundOnDispenser'
""" Транзакция в архиве продаж. Для сверки можно точно брать только
такую транзакцию. """
TRANS_RESULT_FOUND_IN_ARCHIVE         = 'FoundInArchive'
""" Данные о транзакции присутствуют во временной таблице """
TRANS_RESULT_FOUND_IN_TEMPORARY_TABLE = 'FoundInTemporaryTable'
""" Данные о транзакции найдены в "черном ящике" """
TRANS_RESULT_FOUND_IN_BLACKBOX        = 'FoundInBlackBox'
""" Данные о транзакции не найдены """
TRANS_RESULT_NOT_FOUND                = 'NotFound'
""" Идентификатор транзакции не указан в запросе """
TRANS_RESULT_ID_NOT_SPECIFIED         = 'TransIdNotSpecified'

""" Идентификаторы методов вызова к стороннему модулю """
""" Открытие смены """
METHOD_SHIFT_OPEN         = 'ShiftOpen' """ Обязателен к реализации """
""" Закрытие смены """
METHOD_SHIFT_CLOSE        = 'ShiftClose' """ Обязателен к реализации """
""" Получение информации по карте """
METHOD_CARD_INFO          = 'CardInfo'
""" Подготовка операции оплаты """
METHOD_PAYMENT_PREPARE    = 'PaymentPrepare' """ Обязателен к реализации """
""" Подтверждение операции оплаты """
METHOD_PAYMENT_CONFIRM    = 'PaymentConfirm' """ Обязателен к реализации """
""" Подготовка операции возврата """
METHOD_RETURN_PREPARE     = 'ReturnPrepare' """ Обязателен к реализации """
""" Подтверждение операции возврата """
METHOD_RETURN_CONFIRM     = 'ReturnConfirm' """ Обязателен к реализации """
""" Подготовка операции коррекции оплаты """
METHOD_CORRECTION_PREPARE = 'CorrectionPrepare' """ Обязателен к реализации """
""" Подтверждение операции коррекции оплаты """
METHOD_CORRECTION_CONFIRM = 'CorrectionConfirm' """ Обязателен к реализации """
""" Подготовка операции пополнения карты """
METHOD_CREDIT_PREPARE     = 'CreditPrepare'
""" Подтверждение операции пополнения карты """
METHOD_CREDIT_CONFIRM     = 'CreditConfirm'
""" Проведение операции невостребованного возврата """
METHOD_EMERGENCY_RETURN   = 'EmergencyReturn'
""" Успешное завершение транзакции """
METHOD_COMPLETED          = 'Completed' """ Обязателен к реализации """
""" Отмена или откат транзакции """
METHOD_CANCELED           = 'Canceled' """ Обязателен к реализации """

""" Идентификаторы методов обратного вызова к SERVIO PUMP """
""" Получение конфигурации ТРК """
METHOD_GET_FUELLING_POINT_CONFIG = 'GetFuellingPointConfig'
""" Получение конфигурации пистолетов """
METHOD_GET_NOZZLE_CONFIG         = 'GetNozzleConfig'
""" Получение статуса ТРК """
METHOD_GET_FUELLING_POINT_STATUS = 'GetFuellingPointStatus'
""" Получение конфигурации емкостей """
METHOD_GET_TANKS_CONFIG          = 'GetTanksConfig'
""" Получение состояния емкостей """
METHOD_GET_TANK_STATUS           = 'GetTankStatus'
""" Получить список групп товаров/услуг """
METHOD_GET_GOOD_GROUPS           = 'GetGoodGroups'
""" Получение списка доступных товаров/услуг/видов топлива. """
METHOD_GET_GOODS_LIST            = 'GetGoodsList'
""" Получить детальную информацию по одному товару.
Цена текущей партии и остаток. """
METHOD_GET_GOOD_INFO             = 'GetGoodInfo'
""" Получить список оснований """
METHOD_GET_OSNOVAN_LIST          = 'GetOsnovanList'
""" Получить данные о зарегистрированных продажах """
METHOD_DETAILSALES               = 'DetailSales'
""" Установка заказа на ТРК """
METHOD_PRESET                    = 'Preset'
""" Завершение налива на ТРК """
METHOD_END_FILLING               = 'EndFilling'
""" Получить детальные данные о транзакции """
METHOD_GET_TRANSACTION_INFO      = 'GetTransactionInfo'
""" Запись в черный ящик """
METHOD_WRITETOBLACKBOX           = 'WriteToBlackBox'
""" Получить дисконтные схемы """
METHOD_GET_DISCOUNT_SCHEMES      = 'GetDiscountSchemes'
""" Получить лимитные схемы """
METHOD_GET_LIMIT_SCHEMES         = 'GetLimitSchemes'
""" Получить расписания """
METHOD_GET_SCHEDULES             = 'GetSchedules'
""" Получить фискальные документы """
METHOD_GET_FISCAL_RECEIPTS       = 'GetFiscalReceipts'
""" Получить нефискальные документы """
METHOD_GET_NON_FISCAL_RECEIPTS   = 'GetNonFiscalReceipts'
""" Получить информацию по бонусной карте SERVIO PUMP """
METHOD_GET_BONUSES_INFO          = 'GetBonusesInfo'
""" Получение списка фискальных регистраторов """
METHOD_GET_CASH_REGISTERS        = 'GetCashRegisters'
""" Печать нефискального документа """
METHOD_PRINT_NON_FISCAL_DOCUMENT = 'PrintNonFiscalDocument'

""" Список названий тэгов-полей """
""" Метод вызова """
TAG_METHOD                    = 'Method'
""" Код разработчика. Тэг кода разработчика всегда размещается в объекте
верхнего уровня. """
TAG_DEVELOPER_CODE            = 'DeveloperCode'
""" Идентификатор запроса. Указывается в URL запроса. """
TAG_REQUEST_ID                = 'request_id'
""" Фискальные квитанции, напечатанные в процессе транзакции """
TAG_FISCAL_RECEIPTS           = 'FiscalReceipts'
""" Нефискальные квитанции, напечатанные в процессе транзакции """
TAG_NON_FISCAL_RECEIPTS       = 'NonFiscalReceipts'

""" Транзакции. Одновременно в вызов могут приходить три транзакции -
первоначальной оплаты, транзакция коррекции (текущие данные) и
транзакция возврата. Модуль должен ответить системе управления
симметрично с изменением данных и добавлением кода разработчика. """
TAG_TRANSACTIONS              = 'Transactions'
""" Транзакция по-умолчанию """
TAG_TRANSACTION               = 'Transaction'
""" Транзакция оплаты """
TAG_PAYMENT_TRANSACTION       = 'PaymentTransaction'
""" Транзакция возврата """
TAG_RETURN_TRANSACTION        = 'ReturnTransaction'
""" Транзакция коррекции оплаты (по факту налива) """
TAG_CORRECTION_TRANSACTION    = 'CorrectionTransaction'
""" Информация о карте """
TAG_CARDINFO_TRANSACTION      = 'CardInfoTransaction'
""" Открытие смены """
TAG_SHIFT_OPEN_TRANSACTION    = 'ShiftOpenTransaction'
""" Закрытие смены """
TAG_SHIFT_CLOSE_TRANSACTION   = 'ShiftCloseTransaction'
""" Успешное завершение транзакции """
TAG_COMPLETED_TRANSACTION     = 'CompletedTransaction'
""" Откат транзакции """
TAG_CANCELED_TRANSACTION      = 'CanceledTransaction'

""" Далее следуют тэги, общие для большинства транзакций
(см. вызовы METHOD_SHIFT_OPEN, METHOD_SHIFT_CLOSE, METHOD_CARD_INFO,
  METHOD_PAYMENT_PREPARE, METHOD_PAYMENT_CONFIRM, METHOD_RETURN_PREPARE,
  METHOD_RETURN_CONFIRM, METHOD_CORRECTION_PREPARE,
  METHOD_CORRECTION_CONFIRM, METHOD_CREDIT_PREPARE, METHOD_CREDIT_CONFIRM,
  METHOD_EMERGENCY_RETURN, METHOD_COMPLETED, METHOD_CANCELED,
  а также обратный вызов METHOD_PRESET) """
""" Тэги скидки """
""" Позиция скидки """
TAG_D_INDEX                   = 'Index'
""" Идентификатор скидки в рамках транзакции """
TAG_D_DISCOUNT_ID             = 'DiscountId'
""" Тип скидки """
TAG_D_DISCOUNT_TYPE           = 'DiscountType'
""" Размер скидки """
TAG_D_DISCOUNT_VALUE          = 'DiscountValue'
""" Примечание к скидке """
TAG_D_NOTE                    = 'Note'

""" Тэги налоговой ставки """
""" Идентификатор налоговой группы """
TAG_FA_TAX_ID                 = 'TaxId'
""" Название налога """
TAG_FA_TAX_NAME               = 'Name'
""" Налоговая ставка в процентах """
TAG_FA_TAX_RATE               = 'Rate'
""" Примечание """
TAG_FA_TAX_NOTE               = 'Note'

""" Тэги оплаты """
""" Вид оплаты (основание оплаты) """
TAG_P_OSNOVAN_ID              = 'OsnovanId'
""" Название вида оплаты """
TAG_P_OSNOVAN_NAME            = 'OsnovanName'
""" Вид оплаты """
TAG_P_PAYMENT_KIND            = 'PaymentKind'
""" Код эмитента SERVIO PUMP (группа карт) """
TAG_P_ISSUER_ID               = 'IssuerId'
""" Номер карты """
TAG_P_CARDNUMBER              = 'CardNumber'
""" Код клиента SERVIO PUMP """
TAG_P_OWNER_ID                = 'OwnerId'
""" RRN - ссылка на транзакцию во внешней системе """
TAG_P_RRN                     = 'RRN'
""" Данные второй дорожки магнитной полосы """
TAG_P_TRACK2                  = 'Track2'
""" Уникальный номер транзакции со стороны клиента (System Trace Audit Number) """
TAG_P_STAN                    = 'STAN'
""" Код аутентификации """
TAG_P_AUTHCODE                = 'AuthCode'
""" Сумма оплаты бонусами (ранее "кол-во бонусов к списанию", это неверно) """
TAG_P_PRESET_BONUSES          = 'PresetBonuses'
""" Номер телефона клиента (-> ОФД) """
TAG_P_PHONE                   = 'Phone'
""" Электронная почта клиента (-> ОФД) """
TAG_P_EMAIL                   = 'Email'
""" Идентификатор банка SERVIO PUMP """
TAG_P_BANK                    = 'Bank'
""" Хеш номера карты из промежуточного ответа проведения платежа """
TAG_P_HASH                    = 'Hash'
""" ПИН-код карты SERVIO PUMP в кодировке SnS (см. файл UStones.pas) """
TAG_P_PINCODESNS              = 'PinCodeSnS'
""" Сумма, оплаченная наличными """
TAG_P_PAID_CASH               = 'PayedCash'
""" Сумма, оплаченная безналично """
TAG_P_PAID_CASHLESS           = 'PayedCashless'
""" Оплаченная сумма """
TAG_P_PAID_TOTAL              = 'PayedTotal'

""" Тэги транзакции """
""" Дата/время начала смены """
TAG_T_SHIFT_STARTTIME         = 'ShiftStartTime'
""" Дата/время конца смены """
TAG_T_SHIFT_ENDTIME           = 'ShiftEndTime'
""" Номер смены """
TAG_T_SHIFTNUMBER             = 'ShiftNumber'
""" Дата/время начала транзакции """
TAG_T_STARTTIME               = 'StartTime'
""" Дата/время завершения транзакции/смены """
TAG_T_ENDTIME                 = 'EndTime'
""" Номер АЗС """
TAG_T_AZSNUMBER               = 'AZSNumber'
""" Номер транзакции """
TAG_T_TRANS_ID                = 'TransId'
""" Рабочее место """
TAG_T_HOST                    = 'Host'
""" Номер операции """
TAG_T_OP_ID                   = 'OpId'
""" Номер исходной операции """
TAG_T_REF_OP_ID               = 'RefOpId'
""" Имя старшего по смене """
TAG_T_SUPERVISOR              = 'Supervisor'
""" Имя оператора """
TAG_T_OPERATOR                = 'Operator'
""" Код операции терминала """
TAG_T_OPCODE                  = 'OpCode'
""" Код ошибки """
TAG_T_ERRORCODE               = 'ErrorCode'
""" Описание ошибки """
TAG_T_ERRORDESCRIPTION        = 'ErrorDescription'
""" Текст квитанции """
TAG_T_SLIPTEXT                = 'SlipText'
""" Количество позиций """
TAG_T_ITEMCOUNT               = 'ItemCount'
""" Позиции """
TAG_T_ITEMS                   = 'Items'
""" Итого (без учета скидки) """
TAG_T_TOTAL_WO_DISCOUNT       = 'TotalAmountWoDiscount'
""" Кол-во скидок """
TAG_T_DISCOUNT_COUNT          = 'DiscountCount'
""" Скидки """
TAG_T_DISCOUNTS               = 'Discounts'
""" Итого бонусов потрачено """
TAG_T_TOTAL_BONUSES_SPENT     = 'TotalBonusesSpent'
""" Итого бонусов накоплено """
TAG_T_TOTAL_BONUSES_COLLECTED = 'TotalBonusesCollected'
""" Итоговая сумма (с учетом всех скидок) """
TAG_T_TOTAL                   = 'Total'
""" Кол-во платежей """
TAG_T_PAYMENT_COUNT           = 'PaymentCount'
""" Платежи """
TAG_T_PAYMENTS                = 'Payments'
""" Двоичные данные транзакции в кодировке Base64 (1-8 кб).
Например, данные QR-кода. """
TAG_T_BINARYDATA              = 'BinaryData'
""" Фискальные аттрибуты чека """
TAG_T_FISCAL_ATTRIBUTES       = 'FiscalAttributes'

""" Тэги позиции в чеке """
""" Индекс позиции """
TAG_TI_INDEX                  = 'Index'
""" Индекс позиции в связанной транзакции """
TAG_TI_REF_INDEX              = 'RefIndex'
""" Тип позиции """
TAG_TI_KIND                   = 'Kind'
""" Код товара """
TAG_TI_ITEM                   = 'Item'
""" Уникальный идентификатор товара (доп. маркировка) """
TAG_TI_GOODUID                = 'GoodUID'
""" Код группы товара SERVIO PUMP """
TAG_TI_GROUP_ID               = 'GroupId'
""" Код предприятия """
TAG_TI_ENT_ID                 = 'EntId'
""" Название товара """
TAG_TI_NAME                   = 'Name'
""" Сокращенное название товара """
TAG_TI_SHORT_NAME             = 'ShortName'
""" Название единицы измерения """
TAG_TI_UNIT_NAME              = 'UnitName'
""" Номер топливораздаточной колонки """
TAG_TI_FUELLINGPOINT_ID       = 'FuellingPointId'
""" Номер раздаточного крана """
TAG_TI_NOZZLE_ID              = 'NozzleId'
""" Признак: Налив завершен """
TAG_TI_FILLING_COMPLETED      = 'FillingCompleted'
""" Код отдела фискального регистратора """
TAG_TI_DEPARTMENT_ID          = 'DepartmentId'
""" Режим заказа ТРК. см. константы SLT_* """
TAG_TI_PRESET_MODE            = 'PresetMode'
""" Количество(Объем) заказа """
TAG_TI_PRESET_QUANTITY        = 'PresetQuantity'
""" Цена заказа """
TAG_TI_PRESET_PRICE           = 'PresetPrice'
""" Сумма заказа """
TAG_TI_PRESET_AMOUNT          = 'PresetAmount'
""" Значащих десятичных разрядов в записи дробной части количества """
TAG_TI_QUANTITYDECIMALS       = 'QuantityDecimals'
""" Количество или объем """
TAG_TI_QUANTITY               = 'Quantity'
""" Значащих десятичных разрядов в записи дробной части суммы """
TAG_TI_MONEYDECIMALS          = 'MoneyDecimals'
""" Цена без учета скидки (базовая) """
TAG_TI_PRICE_WO_DISCOUNT      = 'PriceWoDiscount'
""" Сумма без учета скидки (по базовой цене) """
TAG_TI_AMOUNT_WO_DISCOUNT     = 'AmountWoDiscount'
""" Кол-во скидок """
TAG_TI_DISCOUNT_COUNT         = 'DiscountCount'
""" Скидки """
TAG_TI_DISCOUNTS              = 'Discounts'
""" Сумма скидок позиции """
TAG_TI_DISCOUNT_AMOUNT        = 'DiscountAmount'
""" Бонусов потрачено """
TAG_TI_BONUSES_SPENT          = 'BonusesSpent'
""" Бонусов накоплено """
TAG_TI_BONUSES_COLLECTED      = 'BonusesCollected'
""" Цена с учетом скидки (итоговая) """
TAG_TI_PRICE                  = 'Price'
"""  Сумма с учетом скидки (по итоговой цене) """
TAG_TI_AMOUNT                 = 'Amount'
""" Двоичные данные позиции в кодировке Base64 (1-8 кб) """
TAG_TI_BINARYDATA             = 'BinaryData'
""" Фискальные аттрибуты позиции """
TAG_TI_FISCAL_ATTRIBUTES      = 'FiscalAttributes'
""" Налоговые ставки позиции """
TAG_TI_TAXES                  = 'Taxes'


""" Тэги конфигурации ТРК
(см. METHOD_GET_FUELLING_POINT_CONFIG, METHOD_GET_NOZZLE_CONFIG) """
""" Минимальный номер ТРК """
TAG_FPC_MINFUELLINGPOINT_ID   = 'MinFuellingPoint'
""" Максимальный номер ТРК """
TAG_FPC_MAXFUELLINGPOINT_ID   = 'MaxFuellingPoint'
""" Количество сторон топливораздаточных колонок """
TAG_FPC_FUELLINGPOINT_COUNT   = 'FuellingPointCount'
""" Массив с конфигурациями ТРК """
TAG_FPC_FUELLINGPOINTS        = 'FuellingPoints'
""" Кол-во пистолетов """
TAG_FPC_NOZZLE_COUNT          = 'NozzleCount'
""" Конфигурация пистолетов ТРК """
TAG_FPC_NOZZLES               = 'Nozzles'
""" Номер ТРК """
TAG_FPC_FUELLINGPOINT_ID      = 'FuellingPointId'
""" Номер РК """
TAG_FPC_NOZZLE_ID             = 'NozzleId'
""" Пистолет заблокирован, отпуск невозможен в данный момент """
TAG_FPC_NOZZLE_LOCKED         = 'NozzleLocked'
""" Номер резервуара """
TAG_FPC_TANK_NO               = 'TankNo'
""" Резервуар заблокирован, отпуск невозможен в данный момент """
TAG_FPC_TANK_LOCKED           = 'TankLocked'
""" Вид - топливо """
TAG_FPC_KIND                  = 'Kind'
""" Код топлива """
TAG_FPC_ITEM                  = 'Item'
""" Название """
TAG_FPC_NAME                  = 'Name'
""" Короткое название """
TAG_FPC_SHORT_NAME            = 'ShortName'
""" Цена """
TAG_FPC_PRICE                 = 'Price'

""" Тэги статуса ТРК (см. METHOD_GET_FUELLING_POINT_STATUS) """
""" Макс. номер ТРК """
TAG_FPS_MINFUELLINGPOINT_ID   = 'MinFuellingPointId'
""" Мин. номер ТРК """
TAG_FPS_MAXFUELLINGPOINT_ID   = 'MaxFuellingPointId'
""" Кол-во ТРК """
TAG_FPS_FUELLINGPOINT_COUNT   = 'FuellingPointCount'
""" Список ТРК """
TAG_FPS_FUELLINGPOINTS        = 'FuellingPoints'
""" Номер ТРК """
TAG_FPS_FUELLINGPOINT_ID      = 'FuellingPointId'
""" Статус ТРК (см. константы FPS_*) """
TAG_FPS_STATUS                = 'Status'
""" Код ошибки ТРК """
TAG_FPS_ERRORCODE             = 'ErrorCode'
""" Номер транзакции """
TAG_FPS_TRANS_ID              = 'TransId'
""" Вид товара (всегда GK_FUEL) """
TAG_FPS_KIND                  = 'Kind'
""" Топливо """
TAG_FPS_ITEM                  = 'Item'
""" Номер крана (0-номер крана неизвестен) """
TAG_FPS_NOZZLE_ID             = 'NozzleId'
""" Цена за литр """
TAG_FPS_PRICE                 = 'Price'
""" Тип лимита заказа (см. константы SLT_*) """
TAG_FPS_STARTLIMITTYPE        = 'StartLimitType'
""" Лимит заказа """
TAG_FPS_STARTLIMIT            = 'StartLimit'
""" Литры """
TAG_FPS_LITERS                = 'Liters'
""" Деньги """
TAG_FPS_MONEY                 = 'Money'


""" Тэги конфигурации емкостей (см. METHOD_GET_TANKS_CONFIG) """
""" Кол-во емкостей """
TAG_TC_TANKCOUNT              = 'TankCount'
""" Список емкостей """
TAG_TC_TANKS                  = 'Tanks'
""" Минимальный номер емкости """
TAG_TC_MINTANK_ID             = 'MinTankId'
""" Максимальный номер емкости """
TAG_TC_MAXTANK_ID             = 'MaxTankId'
""" Номер емкости """
TAG_TC_TANK_ID                = 'TankId'
""" Тип - топливо """
TAG_TC_KIND                   = 'Kind'
""" Код топлива """
TAG_TC_ITEM                   = 'Item'
""" Цена """
TAG_TC_PRICE                  = 'Price'
""" Название """
TAG_TC_NAME                   = 'Name'
""" Аббревиатура """
TAG_TC_SHORT_NAME             = 'ShortName'
""" Минимальный уровень """
TAG_TC_MINLEVEL               = 'MinLevel'
""" Минимальный объем """
TAG_TC_MINVOLUME              = 'MinVolume'
""" Максимальный уровень """
TAG_TC_MAXLEVEL               = 'MaxLevel'
""" Максимальный объем """
TAG_TC_MAXVOLUME              = 'MaxVolume'
""" Объем топлива в трубопроводе """
TAG_TC_TUBEVOLUME             = 'TubeVolume'

""" Тэги состояния емкостей (см. METHOD_GET_TANK_STATUS) """
""" Минимальный номер емкости """
TAG_TS_MINTANK_ID             = 'MinTankId'
""" Максимальный номер емкости """
TAG_TS_MAXTANK_ID             = 'MaxTankId'
""" Номер емкости """
TAG_TS_TANK_ID                = 'TankId'
""" Тип - топливо """
TAG_TS_KIND                   = 'Kind'
""" Код топлива """
TAG_TS_ITEM                   = 'Item'
""" Цена за литр """
TAG_TS_PRICE                  = 'Price'
""" Наименование """
TAG_TS_NAME                   = 'Name'
""" Аббревиатура """
TAG_TS_SHORT_NAME             = 'ShortName'
""" Минимальный уровень """
TAG_TS_MINLEVEL               = 'MinLevel'
""" Минимальный объем """
TAG_TS_MINVOLUME              = 'MinVolume'
""" Максимальный уровень """
TAG_TS_MAXLEVEL               = 'MaxLevel'
""" Максимальный объем """
TAG_TS_MAXVOLUME              = 'MaxVolume'
""" Объем в трубопроводе """
TAG_TS_TUBEVOLUME             = 'TubeVolume'
""" Уровень, мм """
TAG_TS_TOTALLEVEL             = 'TotalLevel'
""" Объем, л """
TAG_TS_TOTALVOLUME            = 'TotalVolume'
""" Объем топлива, л """
TAG_TS_FUELVOLUME             = 'FuelVolume'
""" Плотность топлива, г/см3 """
TAG_TS_FUELDENSITY            = 'FuelDensity'
""" Масса топлива, кг """
TAG_TS_FUELMASS               = 'FuelMass'
""" Уровень воды, мм """
TAG_TS_WATERLEVEL             = 'WaterLevel'
""" Объем воды, л """
TAG_TS_WATERVOLUME            = 'WaterVolume'
""" Температура """
TAG_TS_TEMPERATURE            = 'Temperature'
""" Признак: Емкость заблокирована """
TAG_TS_LOCKED                 = 'Locked'
""" Автокалибровка """
TAG_TS_AUTOCALIBRATING        = 'AutoCalibrating'
""" Прием топлива """
TAG_TS_DELIVERING             = 'Delivering'
""" Несанкционированное наполнение """
TAG_TS_ILLEGALFILLING         = 'IllegalFilling'
""" Утечка """
TAG_TS_LEAKAGE                = 'Leakage'
""" Переполнение """
TAG_TS_OVERFILLING            = 'Overfilling'
""" Высокий уровень воды """
TAG_TS_HIGH_WATER             = 'HighWater'
""" Дата/время последнего обновления данных """
TAG_TS_LASTUPDATE             = 'LastUpdate'


""" Тэги справочника товаров (см. METHOD_GET_GOODS_LIST) """
""" Список товаров """
TAG_G_GOODSLIST               = 'GoodsList'
""" Ограничение по количеству записей """
TAG_G_LIMIT                   = 'Limit'
""" Смещение относительно начала данных """
TAG_G_OFFSET                  = 'Offset'
""" Тип позиции (см. GK_*) """
TAG_G_KIND                    = 'Kind'
""" Код товара/услуги/топлива """
TAG_G_ITEM                    = 'Item'
""" Партия (Дата проведения приходной накладной) """
TAG_G_BATCH_DATE              = 'BatchDate'
""" Группа товара/услуги """
TAG_G_GROUP_ID                = 'GroupId'
""" Название товара """
TAG_G_NAME                    = 'Name'
""" Аббревиатура """
TAG_G_SHORT_NAME              = 'ShortName'
""" Единица измерения """
TAG_G_UNIT_NAME               = 'UnitName'
""" Отдел продажи """
TAG_G_DEPARTMENT_ID           = 'DepartmentId'
""" Отдел возврата """
TAG_G_RETURN_DEPARTMENT_ID    = 'ReturnDepartmentId'
""" Налоговая группа """
TAG_G_TAX_ID                  = 'TaxID'
""" Юр.лицо """
TAG_G_ENT_ID                  = 'EntID'
""" Цена за единицу """
TAG_G_PRICE                   = 'Price'
""" Остаток товара на складе """
TAG_G_REST_QUANTITY           = 'RestQuantity'
""" Разрешена продажа товара по свободной цене """
TAG_G_ARBITRARY_PRICE         = 'ArbitraryPrice'
""" Составной товар """
TAG_G_COMPLEX                 = 'Complex'
""" Примечание """
TAG_G_NOTE                    = 'Note'

""" Тэги данных о конкретном товаре (см. METHOD_GET_GOOD_INFO) """
""" Данные о конкретном товаре """
TAG_GI_GOODINFO              = 'GoodInfo'
""" Тип товара (см. константы GK_*) """
TAG_GI_KIND                  = 'Kind'
""" Код товара """
TAG_GI_ITEM                  = 'Item'
""" Наименование товара """
TAG_GI_NAME                  = 'Name'
""" Код отдела продажи ФР """
TAG_GI_DEPARTMENT_ID         = 'DepartmentId'
""" Код отдела возврата ФР """
TAG_GI_RETURN_DEPARTMENT_ID  = 'ReturnDepartmentId'
""" Цена за единицу """
TAG_GI_PRICE                 = 'Price'
""" Остаток на складе """
TAG_GI_REST_QUANTITY         = 'RestQuantity'
""" Разрешена продажа товара по свободной цене """
TAG_GI_ARBITRARY_PRICE       = 'ArbitraryPrice'
""" Составной товар """
TAG_GI_COMPLEX               = 'Complex'

""" Тэги групп товаров (см. METHOD_GET_GOOD_GROUPS) """
""" Группы товаров/услуг """
TAG_GG_GOOD_GROUPS            = 'GoodGroups'
""" Код родительской группы товаров/услуг """
TAG_GG_PARENT_ID              = 'ParentId'
""" Код группы товаров/услуг """
TAG_GG_GROUP_ID               = 'GroupId'
""" Наименование группы """
TAG_GG_NAME                   = 'Name'

""" Тэги видов оплаты (см. METHOD_GET_OSNOVAN_LIST) """
""" Список оснований оплаты """
TAG_O_OSNOVANLIST             = 'OsnovanList'
""" Внешний код вида оплаты """
TAG_O_OSNOVAN_ID              = 'OsnovanId'
""" Название вида оплаты """
TAG_O_NAME                    = 'Name'
""" Аббревиатура """
TAG_O_SHORT_NAME              = 'ShortName'
""" Вид оплаты (см. константы PK_*) """
TAG_O_PAYMENT_KIND            = 'PaymentKind'
""" Не отображать денежные суммы в отчетах """
TAG_O_NO_MONEY_IN_REPORTS     = 'NoMoneyInReports'
""" Печатать чеки с нулевыми суммами """
TAG_O_ZERO_AMOUNTS_IN_CHEQUE  = 'ZeroAmountsInCheque'
""" Отображать цену в чеках с нулевым итогом """
TAG_O_PRICE_IN_CHEQUE         = 'PriceInCheque'
""" Основание по-умолчанию """
TAG_O_IS_DEFAULT              = 'IsDefault'
""" Основание запрещено """
TAG_O_IS_DISALLOWED           = 'IsDisallowed'
""" Основание скрыто от оператора """
TAG_O_IS_HIDDEN               = 'IsHidden'
""" Для продажи товаров и услуг """
TAG_O_FOR_GOODS_AND_SERVICES  = 'ForGoodsAndServices'
""" Для продажи топлива """
TAG_O_FOR_FUELS               = 'ForFuels'
""" Запретить режим с предоплатой """
TAG_O_DISALLOW_PREPAY_MODE    = 'DisallowPrepayMode'
""" Запретить режим с постоплатой """
TAG_O_DISALLOW_POSTPAY_MODE   = 'DisallowPostpayMode'
""" Код отдела """
TAG_O_DEPARTMENT_ID           = 'DepartmentId'
""" Печатать название основания в чеке """
TAG_O_PRINT_OSNOVAN_NAME      = 'PrintOsnovanName'
""" Топливо возвращается в емкость """
TAG_O_FUEL_RETURNS_TO_TANK    = 'FuelReturnsToTank'
""" Максимальный литровый заказ """
TAG_O_MAX_LITERS_PRESET       = 'MaxLitersPreset'
""" Максимальный денежный заказ """
TAG_O_MAX_MONEY_PRESET        = 'MaxMoneyPreset'
""" Запрет переноса заказа между ТРК """
TAG_O_DISALLOW_MOVE_PRESET    = 'DisallowMovePreset'


""" Тэги архива продаж (см. METHOD_DETAILSALES) """
""" Список зарегистрированных продаж """
TAG_DS_DETAILSALES              = 'DetailSales'
""" Ограничение по количеству выдаваемых записей """
TAG_DS_LIMIT                  = 'Limit'
""" Смещение относительно начала выборки """
TAG_DS_OFFSET                 = 'Offset'
""" Процент налоговой ставки на топливо """
TAG_DS_FUEL_TAX_RATE          = 'FuelTaxRate'
""" Дата/время начала периода """
TAG_DS_DATEFROM               = 'DateFrom'
""" Дата/время конца периода """
TAG_DS_DATETO                 = 'DateTo'
""" Номер АЗС """
TAG_DS_AZSCODE                  = 'AZSCode'
""" Дата/время транзакции """
TAG_DS_DATETIME                 = 'DateTime'
""" Номер транзакции """
TAG_DS_TRANS_ID                 = 'TransId'
""" Рабочее место """
TAG_DS_HOST                     = 'Host'
""" Код операции 0-продажа, 1-возврат """
TAG_DS_OP_CODE                  = 'OpCode'
""" Код группы """
TAG_DS_GROUP_ID                 = 'GroupId'
""" Тип позиции (см. константы GK_*) """
TAG_DS_KIND                     = 'Kind'
""" Код товара/услуги/топлива """
TAG_DS_ITEM                     = 'Item'
""" Дата/время проведения приходной накладной """
TAG_DS_BATCH_DATE               = 'BatchDate'
""" Наименование """
TAG_DS_NAME                     = 'Name'
""" Аббревиатура """
TAG_DS_SHORT_NAME               = 'ShortName'
""" Единица измерения """
TAG_DS_UNIT_NAME                = 'UnitName'
""" Код предприятия """
TAG_DS_ENT_ID                   = 'EntId'
""" Количество (объем) """
TAG_DS_QUANTITY                 = 'Quantity'
""" Цена без скидок """
TAG_DS_PRICE_WO_DISCOUNT        = 'PriceWoDiscount'
""" Сумма по цене без скидок """
TAG_DS_AMOUNT_WO_DISCOUNT       = 'AmountWoDiscount'
""" Скидка с цены в рублях """
TAG_DS_PRICE_DISCOUNT_ABSOLUTE  = 'PriceDiscountAbsolute'
""" Скидка с цены в процентах """
TAG_DS_PRICE_DISCOUNT_PERCENT   = 'PriceDiscountPercent'
""" Скидка с суммы в рублях """
TAG_DS_AMOUNT_DISCOUNT_ABSOLUTE = 'AmountDiscountAbsolute'
""" Скидка с суммы в процентах """
TAG_DS_AMOUNT_DISCOUNT_PERCENT  = 'AmountDiscountPercent'
""" Цена """
TAG_DS_PRICE                    = 'Price'
""" Сумма """
TAG_DS_AMOUNT                   = 'Amount'
""" Сумма скидок """
TAG_DS_DISCOUNT_AMOUNT          = 'DiscountAmount'
""" Код налоговой группы """
TAG_DS_TAX_ID                   = 'TaxId'
""" Налоговая ставка """
TAG_DS_TAX_RATE                 = 'TaxRate'
""" Цена без налогов """
TAG_DS_PRICE_WO_TAXES           = 'PriceWoTaxes'
""" Сумма без налогов """
TAG_DS_AMOUNT_WO_TAXES          = 'AmountWoTaxes'
""" Сумма налогов """
TAG_DS_TAXES_AMOUNT             = 'TaxesAmount'
""" Отдел продажи """
TAG_DS_DEPARTMENT_ID            = 'DepartmentId'
""" Отдел возврата """
TAG_DS_RETURN_DEPARTMENT_ID     = 'ReturnDepartmentId'
""" Вид платежа (см. константы PK_*) """
TAG_DS_PAYMENT_KIND             = 'PaymentKind'
""" Внешний код вида оплаты """
TAG_DS_OSNOVAN_ID               = 'OsnovanId'
""" Название вида оплаты """
TAG_DS_OSNOVAN_NAME             = 'OsnovanName'
""" Номер емкости """
TAG_DS_TANK_ID                  = 'TankId'
""" Номер ТРК """
TAG_DS_FUELLINGPOINT_ID         = 'FuellingPointId'
""" Номер пистолета """
TAG_DS_NOZZLE_ID                = 'NozzleId'
""" Код вида топлива """
TAG_DS_FUEL_ID                  = 'FuelId'
""" Значение суммарного счетчика после окончания налива """
TAG_DS_END_TOTALIZER            = 'EndTotalizer'
""" Режим ограничения на ТРК (см. константы SLT_*) """
TAG_DS_START_LIMIT_TYPE         = 'StartLimitType'
""" Объем или сумма ограничения """
TAG_DS_START_LIMIT              = 'StartLimit'
""" Фактически отпущенный объем топлива """
TAG_DS_VOLUME                   = 'Volume'
""" Объем перелива """
TAG_DS_OVERFILLING              = 'Overfilling'
""" Температура """
TAG_DS_TEMPERATURE              = 'Temperature'
""" Плотность """
TAG_DS_DENSITY                  = 'Density'
""" Масса """
TAG_DS_MASS                     = 'Mass'
""" Примечение """
TAG_DS_NOTE                     = 'Note'
""" Список номеров ФР и чеков """
TAG_DS_RECEIPTS                 = 'Receipts'
""" Список использованных номеров карт и коды их клиентов """
TAG_DS_CARDS                    = 'Cards'


""" Тэг завершения налива (см. METHOD_END_FILLING) """
TAG_EF_TRANS_ID               = 'TransId'

""" Тэги записи сообщения в "черный ящик" АСУ (см. METHOD_WRITETOBLACKBOX) """
""" Сообщение. Максимальная длина сообщения 300 симв. """
TAG_BB_MESSAGE                = 'Message'
""" Номер транзакции """
TAG_BB_TRANS_ID               = 'TransId'
""" Номер ТРК """
TAG_BB_FUELLINGPOINT_ID       = 'FuellingPointId'


""" Тэги получения информации по транзакции (см. METHOD_GET_TRANSACTION_INFO) """
""" Номер транзакции """
TAG_GTI_TRANS_ID                = 'TransId'
""" Дата/время транзакции """
TAG_GTI_DATE_TIME               = 'DateTime'
""" Номер ТРК """
TAG_GTI_FUELLINGPOINT_NO        = 'FuellingPointNo'
""" Внешний код вида топлива """
TAG_GTI_FUEL_NO                 = 'FuelNo'
""" Название вида топлива """
TAG_GTI_FUEL_NAME               = 'FuelName'
""" Номер РК """
TAG_GTI_NOZZLE_NO               = 'NozzleNo'
""" Цена """
TAG_GTI_PRICE                   = 'Price'
""" Текущий объем """
TAG_GTI_REAL_TIME_VOLUME        = 'RealTimeVolume'
""" Текущая сумма """
TAG_GTI_REAL_TIME_MONEY         = 'RealTimeMoney'
""" Объем, зафиксированный во временной таблице. """
TAG_GTI_TEMPORARY_VOLUME        = 'TemporaryVolume'
""" Масса, зафиксированная во временной таблице """
TAG_GTI_TEMPORARY_MASS          = 'TemporaryMass'
""" Сумма, зафиксированная во временной таблице """
TAG_GTI_TEMPORARY_MONEY         = 'TemporaryMoney'
""" Признак: налив завершен. """
TAG_GTI_FILLING_COMPLETED       = 'FillingCompleted'
""" Объем, зафиксированный в архиве продаж """
TAG_GTI_TRANSACTION_VOLUME      = 'TransactionVolume'
""" Признак: транзакция активна? (т.е. находится в процессе выполнения) """
TAG_GTI_TRANSACTION_ACTIVE      = 'TransactionActive'
""" Масса, зафиксированная в архиве продаж """
TAG_GTI_TRANSACTION_MASS        = 'TransactionMass'
""" Сумма, зафиксированная в архиве продаж """
TAG_GTI_TRANSACTION_MONEY       = 'TransactionMoney'
""" Объем, зафиксированный в "черном ящике" АСУ """
TAG_GTI_BLACKBOX_VOLUME         = 'BlackBoxVolume'
""" Объем, зафиксированный в "черном ящике" АСУ """
TAG_GTI_BLACKBOX_MONEY          = 'BlackBoxMoney'
""" Результат завершения транзакции (см. константы TRANS_RESULT_*) """
TAG_GTI_RESULT                  = 'Result'

""" Тэги получения фискальных документов (см. METHOD_GET_FISCAL_RECEIPTS) """
""" Фискальные документы """
TAG_GFR_FISCAL_RECEIPTS         = 'FiscalReceipts'
""" Номер транзакции """
TAG_GFR_TRANS_ID                = 'TransId'
""" Дата/время начала периода """
TAG_GFR_DATE_FROM               = 'DateFrom'
""" Дата/время окончания периода """
TAG_GFR_DATE_TO                 = 'DateTo'

""" Тэги получения нефискальных документов
(см. METHOD_GET_NON_FISCAL_RECEIPTS) """
""" Нефискальные документы """
TAG_GNFR_NON_FISCAL_RECEIPTS    = 'NonFiscalReceipts'
""" Номер транзакции """
TAG_GNFR_TRANS_ID               = 'TransId'
""" Дата/время начала периода """
TAG_GNFR_DATE_FROM              = 'DateFrom'
""" Дата/время окончания периода """
TAG_GNFR_DATE_TO                = 'DateTo'

""" Тэги дисконтных схем (см. METHOD_GET_DISCOUNT_SCHEMES) """
""" Идентификатор дисконтной схемы """
TAG_DS1_DISCOUNT_SCHEME_ID       = 'DiscountSchemeId'
""" Список дисконтных схем """
TAG_DS1_DISCOUNT_SCHEMES         = 'DiscountSchemes'
""" Название дисконтной схемы """
TAG_DS1_NAME                    = 'Name'
""" Примечание к дисконтной схеме """
TAG_DS1_NOTE                    = 'Note'
""" Дата/время окончания срока действия дисконтной схемы """
TAG_DS1_EXPIRY_DATE              = 'ExpiryDate'
""" Список элементов дисконтной схемы """
TAG_DS1_ITEMS                    = 'Items'
""" Тип позиции (см. константы GK_*) """
TAG_DSI_GOOD_KIND               = 'GoodKind'
""" Код позиции дисконтной схемы """
TAG_DSI_GOOD_ID                 = 'GoodId'
""" Порог дисконтной схемы """
TAG_DSI_THRESHOLD               = 'Threshold'
""" Тип скидки дисконтной схемы (см. константы DISCOUNT_KIND_*) """
TAG_DSI_DISCOUNT_KIND           = 'DiscountKind'
""" Скидка с цены в процентах """
TAG_DSI_PRICE_DISCOUNT_PERCENT  = 'PriceDiscountPercent'
""" Скидка с цены в абсолютном выражении """
TAG_DSI_PRICE_DISCOUNT_ABSOLUTE = 'PriceDiscountAbsolute'
""" Фиксированная цена """
TAG_DSI_FIXED_PRICE             = 'FixedPrice'

""" Тэги лимитных схем (см. METHOD_GET_LIMIT_SCHEMES) """
""" Список схем лимитов """
TAG_LS_LIMIT_SCHEMES            = 'LimitSchemes'
""" Идентификатор схемы лимитов """
TAG_LS_LIMITSCHEME_ID           = 'LimitSchemeId'
""" Название схемы лимитов """
TAG_LS_NAME                     = 'Name'
""" Примечание к схеме лимитов """
TAG_LS_NOTE                     = 'Note'
""" Список позиций схемы лимитов """
TAG_LS_ITEMS                    = 'Items'
""" Тип позиции схемы лимитов (см. константы GK_*) """
TAG_LSI_GOOD_KIND                = 'GoodKind'
""" Код позиции схемы лимитов """
TAG_LSI_GOOD_ID                  = 'GoodId'
""" Лимит заказа """
TAG_LSI_ORDER_LIMIT              = 'OrderLimit'
""" Суточный лимит """
TAG_LSI_DAY_LIMIT                = 'DayLimit'
""" Месячный лимит """
TAG_LSI_MONTH_LIMIT              = 'MonthLimit'
""" Общий лимит """
TAG_LSI_TOTAL_LIMIT              = 'TotalLimit'

""" Тэги расписаний (см. METHOD_GET_SCHEDULES) """
""" Список расписаний """
TAG_SCH_SCHEDULES         = 'Schedules'
""" Идентификатор расписания """
TAG_SCH_SCHEDULE_ID       = 'ScheduleId'
""" Название расписания """
TAG_SCH_NAME              = 'Name'
""" Схема расписания (см. константы SCHEDULE_SCHEME_*) """
TAG_SCH_SCHEME            = 'Scheme'
""" Выбранные дни недели - список через запятую (см. константы WEEKDAY_*) """
TAG_SCH_CHOOSEN_WEEK_DAYS = 'ChoosenWeekDays'
""" Список диапазонов дат """
TAG_SCH_DATE_RANGES       = 'DateRanges'
""" Начало периода дат """
TAG_SCH_DATE_FROM         = 'DateFrom'
""" Конец периода дат """
TAG_SCH_DATE_TO           = 'DateTo'
""" Список диапазонов времени """
TAG_SCH_TIME_RANGES       = 'TimeRanges'
""" Начало периода времени """
TAG_SCH_TIME_FROM         = 'TimeFrom'
""" Конец периода времени """
TAG_SCH_TIME_TO           = 'TimeTo'

""" Тэги информации по бонусной карте SERVIO PUMP
(см. METHOD_GET_BONUSES_INFO) """
""" Информация по бонусной карте """
TAG_GBI_BONUSES_INFO      = 'BonusesInfo'
""" Код эмитента карты """
TAG_GBI_ISSUER_ID         = 'IssuerId'
""" Номер карты """
TAG_GBI_CARD_NO           = 'CardNo'
""" Текст квитанции с информацией по карте """
TAG_GBI_SLIP_TEXT         = 'SlipText'
""" Сумма, доступная для оплаты бонусами. Сумма оплаты бонусами в
конкретной транзакции может быть меньше данного значения. """
TAG_GBI_BONUS_MONEY       = 'BonusMoney'
""" Код ошибки выполнения операции.
Коды ошибок универсального терминала ERROR_* """
TAG_GBI_ERRORCODE         = 'ErrorCode'
""" Описание ошибки """
TAG_GBI_DESCRIPTION       = 'Description'

""" Тэги получения списка фискальных регистраторов """
""" Список фискальных регистраторов """
TAG_GCR_CASH_REGISTERS    = 'CashRegisters'
""" Название фискального регистратора """
TAG_GCR_DEVICE_NAME       = 'DeviceName'

""" Тэги печати нефискального документа """
""" Название устройства для печати документа """
TAG_PNFD_DEVICE_NAME      = 'DeviceName'
""" Строки нефискального документа, разделенные символом | для печати на кассе """
TAG_PNFD_SLIP_TEXT          = 'SlipText'

""" Фискальные аттрибуты исключены из документации на данный момент. """

""" Справочник кодов ошибок и их описаний """
""" Общие коды ошибок """
ERROR_OK                               = 0
S_ERROR_OK                             = 'Нет ошибки. Операция выполнена успешно.'

ERROR_CANCEL                           = 2
S_ERROR_CANCEL                         = 'Выполнение операции прервано оператором'

""" Коды ошибок драйвера (интерфейса с SERVIO PUMP) """
ERROR_TRANSCODE_EXTCODE_TO_DEVCODE     = 1001
S_ERROR_TRANSCODE_EXTCODE_TO_DEVCODE   = 'Ошибка при перекодировании внешнего кода (%s) в код для устройств !'

ERROR_TRANSCODE_DEVCODE_TO_EXTCODE     = 1002
S_ERROR_TRANSCODE_DEVCODE_TO_EXTCODE   = 'Ошибка при перекодировании кода для устройств (%s) во внешний код !'

ERROR_MAX_ITEMS                        = 1003
S_ERROR_MAX_ITEMS                      = 'Превышено максимально допустимое количество позиций чека !'

ERROR_GOOD_NOT_FOUND                   = 1006
S_ERROR_GOOD_NOT_FOUND                 = 'Товар не найден в справочнике !'

ERROR_CANT_CONNECT_TO_DATABASE         = 1007
S_ERROR_CANT_CONNECT_TO_DATABASE       = 'Невозможно подключиться к базе данных !'

""" Коды ошибок терминала (внутреннего объекта) """
ERROR_DATABASE_CONNECTION         = 101
S_DATABASE_CONNECTION             = 'Ошибка при подключении к базе данных. Проверьте параметры подключения.'

ERROR_MODULE_LOAD                 = 102
S_ERROR_MODULE_LOAD               = 'При загрузке внешней библиотеки произошла ошибка.'

ERROR_OPERATION_NOT_IMPLEMENTED   = 103
S_ERROR_OPERATION_NOT_IMPLEMENTED = 'Операция не поддерживается в текущей реализации'

ERROR_METHOD_NOT_IMPLEMENTED      = 104
S_ERROR_METHOD_NOT_IMPLEMENTED    = 'Метод "%s" не поддерживается в текущей реализации'

ERROR_PRESET_NOT_FOUND            = 105
S_ERROR_PRESET_NOT_FOUND          = 'Не удалось загрузить информацию о заказе активного терминала из базы данных.'

ERROR_HTTP_CLIENT_INIT            = 106
S_ERROR_HTTP_CLIENT_INIT          = 'Ошибка при инициализации HTTP(S)-клиента'

ERROR_HTTP_SERVER_INIT            = 107
S_ERROR_HTTP_SERVER_INIT          = 'Ошибка при инициализации HTTP(S)-сервера'

ERROR_SAVING_PAYMENT_PREPARE      = 108
S_ERROR_SAVING_PAYMENT_PREPARE    = 'Ошибка при сохранении транзакции (этап расчета скидок)'

ERROR_LOADING_PAYMENT_PREPARE     = 109
S_ERROR_LOADING_PAYMENT_PREPARE   = 'Ошибка при загрузке транзакции (этапа расчета скидок)'

ERROR_SAVING_PAYMENT_CONFIRM      = 110
S_ERROR_SAVING_PAYMENT_CONFIRM    = 'Ошибка при сохранении транзакции (этап подтверждения оплаты)'

ERROR_LOADING_PAYMENT_CONFIRM     = 111
S_ERROR_LOADING_PAYMENT_CONFIRM   = 'Ошибка при загрузке транзакции (этапа подтверждения оплаты)'

ERROR_SAVING_RETURN_PREPARE       = 112
S_ERROR_SAVING_RETURN_PREPARE     = 'Ошибка при сохранении транзакции (этап возврата оплаты)'

ERROR_SAVING_RETURN_CONFIRM       = 113
S_ERROR_SAVING_RETURN_CONFIRM     = 'Ошибка при сохранении транзакции (этап отмены расчета скидок)'

ERROR_SAVING_CREDIT_PREPARE       = 114
S_ERROR_SAVING_CREDIT_PREPARE     = 'Ошибка при сохранении транзакции (этап подготовки пополнения карты)'

ERROR_SAVING_CREDIT_CONFIRM       = 115
S_ERROR_SAVING_CREDIT_CONFIRM     = 'Ошибка при сохранении транзакции (этап подтверждения пополнения карты)'

ERROR_SAVING_SHIFT_OPEN           = 116
S_ERROR_SAVING_SHIFT_OPEN         = 'Ошибка при сохранении транзакции (этап открытия смены)'

ERROR_SAVING_SHIFT_CLOSE          = 117
S_ERROR_SAVING_SHIFT_CLOSE        = 'Ошибка при сохранении транзакции (этап открытия смены)'

ERROR_SAVING_CARDINFO             = 118
S_ERROR_SAVING_CARDINFO           = 'Ошибка при сохранении транзакции (этап сохранения информации по карте)'

ERROR_HOST_NOT_SPECIFIED          = 119
S_ERROR_HOST_NOT_SPECIFIED        = 'Не указано рабочее место, с которого производится операция !'

ERROR_AZSNUMBER_NOT_SPECIFIED     = 120
S_ERROR_AZSNUMBER_NOT_SPECIFIED   = 'Не указан номер объекта АЗС, с которого производится операция !'

ERROR_NO_TRANS_ID                 = 121
S_ERROR_NO_TRANS_ID               = 'Номер транзакции не указан или указан неверно !'

ERROR_NO_ITEMS                    = 122
S_ERROR_NO_ITEMS                  = 'В транзакции нет позиций !'

ERROR_GOOD_CODE_LEN               = 123
S_ERROR_GOOD_CODE_LEN             = 'Код товара не указан или длина кода товара слишком большая !'

ERROR_ITEM_NAME_TOO_LONG          = 124
S_ERROR_ITEM_NAME_TOO_LONG        = 'Название позиции слишком длинное'

ERROR_PRICE_WO_DISCOUNT           = 125
S_ERROR_PRICE_WO_DISCOUNT         = 'Базовая цена не может быть меньше нуля'

ERROR_QUANTITY                    = 126
S_ERROR_QUANTITY                  = 'Количество товара или объем топлива не может быть меньше или равен нулю !'

ERROR_FUELLINGPOINT_ID            = 127
S_ERROR_FUELLINGPOINT_ID          = 'Номер топливораздаточной колонки указан неверно !'

ERROR_BONUSES_SPENT               = 128
S_ERROR_BONUSES_SPENT             = 'Количество потраченных бонусов не может быть меньше нуля !'

ERROR_BONUSES_COLLECTED           = 129
S_ERROR_BONUSES_COLLECTED         = 'Количество накопленных бонусов не может быть меньше нуля !'

ERROR_PAYED_ITEM_NOT_FOUND        = 130
S_ERROR_PAYED_ITEM_NOT_FOUND      = 'Позиция к возврату не найдена в первоначальной транзакции оплаты !'

ERROR_NO_RETURN_ITEMS             = 131
S_ERROR_NO_RETURN_ITEMS           = 'Нет позиций к возврату !'

ERROR_RITEM_PRICE_WO_DISCOUNT     = 132
S_ERROR_RITEM_PRICE_WO_DISCOUNT   = 'Цена товара на этапе возврата отличается от цены товара на этапе продажи !'

ERROR_RITEM_QUANTITY              = 133
S_ERROR_RITEM_QUANTITY            = 'Кол-во товара к возврату больше чем кол-во проданного товара !'

ERROR_REFUND_OSNOVAN_ID           = 134
S_ERROR_REFUND_OSNOVAN_ID         = 'Вид оплаты на этапе возврата отличается от вида оплаты на этапе продажи !'

ERROR_REFUND_CARDNO               = 135
S_ERROR_REFUND_CARDNO             = 'Номер карты на этапе возврата отличается от номера карты на этапе продажи !'

ERROR_ROWNER_ID                   = 136
S_ERROR_ROWNER_ID                 = 'Код клиента на этапе возврата отличается от кода клиента на этапе продажи !'

ERROR_NO_COMMUNICATION_CANCEL     = 137
S_ERROR_NO_COMMUNICATION_CANCEL   = 'Нет связи с удаленным сервером. Отмена операции.'

ERROR_RPAYMENT                    = 138
S_ERROR_RPAYMENT                  = 'Виды оплаты, указанные на этапе возврата не соответствуют видам оплаты на этапе продажи !'

ERROR_MODULE_INIT                 = 139
S_ERROR_MODULE_INIT               = 'Ошибка при инициализации внешней библиотеки !'

ERROR_PITEM_NOT_FOUND             = 140
S_ERROR_PITEM_NOT_FOUND           = 'Корректируемая позиция не найдена в транзакции продажи !'

ERROR_TRANSACTION_NOT_FOUND       = 141
S_ERROR_TRANSACTION_NOT_FOUND     = 'Транзакция не найдена !'

ERROR_MOP_ID                      = 142
S_ERROR_MOP_ID                    = 'Код основания "%d" оплаты указан неверно !'

ERROR_NO_PAYMENTS                 = 143
S_ERROR_NO_PAYMENTS               = 'Транзакция не содержит видов оплаты !'

ERROR_TRANS_REJECTED              = 144
S_ERROR_TRANS_REJECTED            = 'Транзакция отклонена SERVIO PUMP !'

ERROR_REQUEST_ID_NOT_UNIQUE       = 145
S_ERROR_REQUEST_ID_NOT_UNIQUE     = 'Запрос с указанным request_id уже был выполнен !'

ERROR_POST_STREAM_TOO_LARGE       = 146
S_ERROR_POST_STREAM_TOO_LARGE     = 'Объем POST-данных слишком велик !'

ERROR_REQUEST_PARSING_ERROR       = 147
S_ERROR_REQUEST_PARSING_ERROR     = 'Ошибка разбора запроса !'

ERROR_POST_STREAM_IS_NULL         = 148
S_ERROR_POST_STREAM_IS_NULL       = 'POST-данные не указаны в запросе !'

ERROR_PRESET_FAILED               = 149
S_ERROR_PRESET_FAILED             = 'Установка заказа завершена с ошибкой !'

ERROR_UNSUPPORTED_OPCODE          = 150
S_ERROR_UNSUPPORTED_OPCODE        = 'Код операции не поддерживается !'

ERROR_INVALID_INPUT_STRUCTURE     = 151
S_ERROR_INVALID_INPUT_STRUCTURE   = 'Ошибка входной структуры !'

ERROR_DEVELOPER_CODE_NOT_FOUND    = 152
S_ERROR_DEVELOPER_CODE_NOT_FOUND  = 'Код разработчика не найден !'

ERROR_DEVELOPER_CODE_CHECK_ERROR  = 153
S_ERROR_DEVELOPER_CODE_CHECK_ERROR = 'Ошибка при проверке кода разработчика !'

ERROR_PROTECTION_VIOLATION        = 154
S_ERROR_PROTECTION_VIOLATION      = 'Нарушение защиты программы !'

ERROR_INVALID_DEVELOPER_CODE      = 155
S_ERROR_INVALID_DEVELOPER_CODE    = 'Некорректный код разработчика !'

ERROR_NOT_ENOUGH_GOODS_IN_STOCK   = 156
S_ERROR_NOT_ENOUGH_GOODS_IN_STOCK = 'Не достаточно товара на складе !'

ERROR_NO_COMMUNICATION_SKIP       = 157
S_ERROR_NO_COMMUNICATION_SKIP     = 'Нет связи с удаленным сервером. Пропуск операции по терминалу.'

init_fn_s          = 'Init'
deinit_fn_s        = 'Deinit'
call_fn_s          = 'Call'
free_response_fn_s = 'FreeResponse'
set_callback_fn_s  = 'SetCallback'
