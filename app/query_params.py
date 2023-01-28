from drf_yasg import openapi


def mahsulot_olchov_query_params():
    olchov = openapi.Parameter(
        "olchov", openapi.IN_QUERY, description="olchov id si", type=openapi.TYPE_STRING)
    narx = openapi.Parameter("narx", openapi.IN_QUERY,
                             description="narx", type=openapi.TYPE_STRING)
    return [olchov, narx]


def import_export_query_params():
    mahsulot_nomi = openapi.Parameter("mahsulot_nomi", openapi.IN_QUERY, description="mahsulot_nomi",
                                      type=openapi.TYPE_STRING)
    format = openapi.Parameter(
        "format", openapi.IN_QUERY, description="format", type=openapi.TYPE_STRING)
    miqdor = openapi.Parameter(
        "miqdor", openapi.IN_QUERY, description="miqdor", type=openapi.TYPE_INTEGER)
    vaqt = openapi.Parameter("import_vaqt", openapi.IN_QUERY, description="import_vaqt format (yyyy-mm-dd)",
                             type=openapi.TYPE_INTEGER)

    return [mahsulot_nomi, format, miqdor, vaqt]


def customer_query_params():
    nomi = openapi.Parameter("nomi", openapi.IN_QUERY,
                             description="nomi", type=openapi.TYPE_STRING)
    ism_sharif = openapi.Parameter(
        "ism_sharif", openapi.IN_QUERY, description="ism_sharif", type=openapi.TYPE_STRING)

    telefon = openapi.Parameter(
        "telefon", openapi.IN_QUERY, description="telefon", type=openapi.TYPE_STRING)
    status = openapi.Parameter(
        "status", openapi.IN_QUERY, description="status", type=openapi.TYPE_INTEGER)
    bonus = openapi.Parameter(
        "bonus", openapi.IN_QUERY, description="bonus_id", type=openapi.TYPE_INTEGER)
    return [nomi, ism_sharif, telefon,status, bonus]


def order_query_params():
    
    buyurtma_nomi = openapi.Parameter(
        "buyurtma_nomi", openapi.IN_QUERY, description="buyurtma id si", type=openapi.TYPE_INTEGER)
    
    mijoz = openapi.Parameter(
        "mijoz", openapi.IN_QUERY, description="mijoz id si", type=openapi.TYPE_INTEGER)
    format = openapi.Parameter(
        "format", openapi.IN_QUERY, description="format", type=openapi.TYPE_STRING)
    buyurtma_olchov = openapi.Parameter(
        "buyurtma_olchov", openapi.IN_QUERY, description="buyurtma_olchov", type=openapi.TYPE_STRING)
    
    narx = openapi.Parameter(
        "narx", openapi.IN_QUERY, description="narx", type=openapi.TYPE_STRING)
    
    miqdor = openapi.Parameter(
        "miqdor", openapi.IN_QUERY, description="miqdor", type=openapi.TYPE_STRING)
    
    count = openapi.Parameter(
        "count", openapi.IN_QUERY, description="count", type=openapi.TYPE_STRING)
        
    buyurtma_sana = openapi.Parameter("buyurtma_sana", openapi.IN_QUERY,
                                      description="buyurtma_sana format (yyyy-mm-dd)",
                                      type=openapi.TYPE_STRING)
    return [buyurtma_nomi,mijoz, format, buyurtma_sana, buyurtma_olchov, narx, miqdor, count]


def bonus_query_params():
    bonus_nomi = openapi.Parameter(
        "bonus_nomi", openapi.IN_QUERY, description="bonus_nomi", type=openapi.TYPE_STRING)
    bonus_miqdori = openapi.Parameter(
        "bonus_miqdori", openapi.IN_QUERY, description="bonus_miqdori", type=openapi.TYPE_STRING)
    bonus_muddati = openapi.Parameter(
        "bonus_muddati", openapi.IN_QUERY, description="bonus_muddati", type=openapi.TYPE_STRING)

    return [bonus_nomi, bonus_miqdori, bonus_muddati]


def mahsulot_query_params():
    mahsulot_nomi = openapi.Parameter(
        "mahsulot_olchov", openapi.IN_QUERY, description="mahsulot_olchov", type=openapi.TYPE_INTEGER)
    mahsulot_format = openapi.Parameter(
        "mahsulot_format", openapi.IN_QUERY, description="mahsulot_format", type=openapi.TYPE_STRING)

    return mahsulot_nomi, mahsulot_format


def mahsulot_olchov_query_params():
    olchov = openapi.Parameter("olchov", openapi.IN_QUERY, description="olchov id si", type=openapi.TYPE_STRING)
    olchov = openapi.Parameter("olchov", openapi.IN_QUERY, description="olchov", type=openapi.TYPE_STRING)
    narx = openapi.Parameter("narx", openapi.IN_QUERY, description="narx", type=openapi.TYPE_STRING)
    mahsulot_number = openapi.Parameter("mahsulot_number", openapi.IN_QUERY,
                                        description="mahsulot_number", type=openapi.TYPE_INTEGER)

    return [olchov, narx, mahsulot_number]


def worker_query_params():
    lavozim = openapi.Parameter(
        "lavozim", openapi.IN_QUERY, description="lavozim", type=openapi.TYPE_STRING)
    ism_sharif = openapi.Parameter(
        "ism_sharif", openapi.IN_QUERY, description="ism_sharif", type=openapi.TYPE_STRING)

    oylik = openapi.Parameter(
        "oylik", openapi.IN_QUERY, description="oylik", type=openapi.TYPE_STRING)

    stavka = openapi.Parameter(
        "stavka", openapi.IN_QUERY, description="stavka", type=openapi.TYPE_INTEGER)

    return [ism_sharif, lavozim, oylik, stavka]



def moliya_kirim_query_params():
    tranzaksiya_turi = openapi.Parameter("tranzaksiya_turi", openapi.IN_QUERY, description="tranzaksiya_turi uchun", type=openapi.TYPE_STRING)
    mijoz = openapi.Parameter("mijoz", openapi.IN_QUERY, description="mijoz uchun", type=openapi.TYPE_STRING)
    tolov_turi = openapi.Parameter("tolov_turi", openapi.IN_QUERY, description="tolov_turi uchun", type=openapi.TYPE_STRING)
    summa = openapi.Parameter("summa", openapi.IN_QUERY, description="summa", type=openapi.TYPE_STRING)                          
    vaqt = openapi.Parameter("vaqt", openapi.IN_QUERY, description="vaqt", type=openapi.TYPE_STRING)
    description = openapi.Parameter("description", openapi.IN_QUERY, description="description", type=openapi.TYPE_STRING) 
    return [tranzaksiya_turi, mijoz, tolov_turi,summa,vaqt,description]


def moliya_chiqim_query_params():
    tranzaksiya_turi = openapi.Parameter("tranzaksiya_turi", openapi.IN_QUERY, description="tranzaksiya_turi uchun", type=openapi.TYPE_STRING)
    mijoz = openapi.Parameter("mijoz", openapi.IN_QUERY, description="mijoz uchun", type=openapi.TYPE_STRING)

    hodim = openapi.Parameter("hodim", openapi.IN_QUERY, description="hodim uchun", type=openapi.TYPE_STRING)
    mahsulot_nomi = openapi.Parameter("mahsulot_nomi", openapi.IN_QUERY, description="mahsulot_nomi uchun", type=openapi.TYPE_STRING)
    format = openapi.Parameter("format", openapi.IN_QUERY, description="format uchun", type=openapi.TYPE_STRING)
    mahsulot_olchov = openapi.Parameter("mahsulot_olchov", openapi.IN_QUERY, description="mahsulot_olchov uchun", type=openapi.TYPE_STRING)
    narx = openapi.Parameter("narx", openapi.IN_QUERY, description="narx uchun", type=openapi.TYPE_STRING)
    miqdor = openapi.Parameter("narx", openapi.IN_QUERY, description="narx uchun", type=openapi.TYPE_STRING)
    tolov_turi = openapi.Parameter("tolov_turi", openapi.IN_QUERY, description="tolov_turi uchun", type=openapi.TYPE_STRING)
    umumiy = openapi.Parameter("umumiy", openapi.IN_QUERY, description="umumiy", type=openapi.TYPE_STRING)                          
    vaqt = openapi.Parameter("vaqt", openapi.IN_QUERY, description="vaqt", type=openapi.TYPE_STRING)
    description = openapi.Parameter("description", openapi.IN_QUERY, description="description", type=openapi.TYPE_STRING) 
    return [tranzaksiya_turi, mijoz, hodim , mahsulot_nomi, format, mahsulot_olchov ,narx,miqdor, tolov_turi,umumiy,vaqt,description]



def ombor_query_params():
    mahsulot = openapi.Parameter(
        "mahsulot", openapi.IN_QUERY, description="mahsulot", type=openapi.TYPE_STRING)
    format = openapi.Parameter(
        "format", openapi.IN_QUERY, description="format", type=openapi.TYPE_STRING)
    olchov = openapi.Parameter(
        "olchov", openapi.IN_QUERY, description="olchov", type=openapi.TYPE_STRING)
    narx = openapi.Parameter(
        "narx", openapi.IN_QUERY, description="narx", type=openapi.TYPE_STRING)
    miqdor = openapi.Parameter(
        "miqdor", openapi.IN_QUERY, description="miqdor", type=openapi.TYPE_STRING)

    return [mahsulot, format, olchov,narx,miqdor]