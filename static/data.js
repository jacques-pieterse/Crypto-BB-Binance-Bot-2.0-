window.onload = setupRefresh;
    function setupRefresh()
    {
        setInterval("refreshBlock();",5000);
    }
    
    function refreshBlock()
    {
       $('#coin-info').load("/coin-data");
       $('#usd-info').load("/usd-data");
    }