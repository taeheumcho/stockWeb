// strategy 초기 전략 설정을 위한 기본 정보 입력

function submit() {
       
    asset_data = $('#example').find('tbody tr')
    period_data = $('#step-2').find('span')
    timelag=$('#timelag').find('input').val()
    strategyNum = $('#strategyNum').find('h4')
    port_param = ''
    weight_param = ''
    asset_data2 = $('.checked')
    verified = true

    if(timelag == 0){
    	alert('time lag를 입력해주세요');
    	return;
    }
    
    assetcode = []
    for (i = 0 ; i < asset_data2.length; i++){
    	asset_code_imsi = $(asset_data2[i]).find('input')
    	asset_code_val = $(asset_code_imsi).val()
    	assetcode.push(asset_code_val)
//    	if($(assets[0]).find('div').className == 'icheckbox_flat-green checked'){
//    		assetcode.push($(assets[1]).text())
//    	}
        if (i != asset_data2.length - 1) {
            port_param += asset_code_val + '|'
        } else {
            port_param += asset_code_val
        }   
    }
    
    if(assetcode.length == 0){
    	alert('asset을 선택해주세요');
    	return;
    }
    strategy_Num = -1
    for (i = 0 ; i < strategyNum.length; i++){
//    	numImsi = $((strategyNum[i]).attributes[5]).val()
    	numImsi = $((strategyNum[i]).attributes[5]).val()
    	
    	if (numImsi != "false"){
    		strategy_Num = "" + i
    	}
    }
    if(strategy_Num == "-1"){
    	alert('전략을 선택해주세요');
    	return;
    }
//    // 포트 입력
//    for (i = 0; i < trs.length ; i++) {
//        console.log($(trs[i]).html())
//        tds = $(trs[i]).find('td')
//        gicode = $(tds[1]).text()
//        weight = $(tds[3]).find('input').val()
//        
//        if (weight.trim() == '') {
//            alert('비중을 입력하세요.');
//            verified = false;
//            return;
//        }
//
//        if (i != trs.length - 1) {
//            port_param += gicode + '|'
//            weight_param += weight + '|'
//        } else {
//            port_param += gicode
//            weight_param += weight
//        }        
//    }

//    if (verified) {
//        $('#loader').show();
//        $('#input_port').val(port_param)
//        $('#input_wgt').val(weight_param)
//        $('#input_bm').val($('#button-bm').text().trim())
//        $('#form_report').submit();
//    }
    
    if (verified) {
        
        $('#input_assets').val(port_param)
        $('#input_training').val(period_data[0].innerHTML)
        $('#input_test').val(period_data[1].innerHTML)
        $('#input_timelag').val(timelag)
        $('#input_strategy').val(strategy_Num)
        $('#form_report').submit();
    }

}

function validate_date(value) {
    var re = /^\d{4}-\d{1,2}-\d{1,2}$/;
    // valid if optional and empty OR if it passes the regex test
    //return (this.optional(element) && value == "") || re.test(value);
    return re.test(value);
}

$("#form_report").bind('ajax:complete', function () {

    // tasks to do 
    $('#loader').hide();
});


function refresh_t0() {

    inputed_dt = $('#input-initial-date').val()
    listed_dt_list = $('.listed_dt')

    //alert('input : ' + inputed_dt);
    if (listed_dt_list.length >= 1) {        
        target_dt = $(listed_dt_list[0]).text()
        console.log(target_dt)
        for (i = 0; i < listed_dt_list.length - 1; i++) {            
            listed_dt = $(listed_dt_list[i]).text();
            if (listed_dt >= target_dt) {
                target_dt = listed_dt
            }            
        }        
        
        // alert('target:' + target_dt + ' inputed:' + inputed_dt)
        if (datestr_date(target_dt, '-') >= datestr_date(inputed_dt), '-') {
            $('#input_t0').val(target_dt)
            $('#input-initial-date').val(target_dt)
        }
        
    }
    else {
        $('#input_t0').val('2005-01-01')
        $('#input-initial-date').val('2005-01-01')
    }
}

function datestr_date(dt_str, splitor) {
    from = dt_str.split(splitor);
    f = new Date(from[2], from[1] - 1, from[0]);
    return f
}